"""Minimal self-learning agent: act -> reflect -> remember -> act better next time."""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import anthropic

MODEL = os.getenv("AGENT_MODEL", "claude-sonnet-5-5")
MEMORY_FILE = Path("lessons.json")
MAX_STEPS = 8
MAX_LESSONS_IN_PROMPT = 10

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment


# ---------- Memory ----------
def load_lessons() -> list[dict]:
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text())
    return []


def save_lesson(task: str, lesson: str) -> None:
    lessons = load_lessons()
    lessons.append({"task": task, "lesson": lesson})
    MEMORY_FILE.write_text(json.dumps(lessons, indent=2))


# ---------- Tools ----------
TOOLS = [
    {
        "name": "run_python",
        "description": "Run a Python script and return its stdout/stderr. Use print() to see results.",
        "input_schema": {
            "type": "object",
            "properties": {"code": {"type": "string", "description": "Python code to run"}},
            "required": ["code"],
        },
    }
]


def run_python(code: str) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name
    try:
        result = subprocess.run(
            [sys.executable, path], capture_output=True, text=True, timeout=10
        )
        return (result.stdout + result.stderr).strip() or "(no output)"
    except subprocess.TimeoutExpired:
        return "Error: script timed out after 10 seconds"
    finally:
        os.unlink(path)


# ---------- Agent loop ----------
def build_system_prompt(lessons: list[dict]) -> str:
    prompt = "You are a careful Python problem-solving agent. Test your code with the run_python tool before giving a final answer."
    if lessons:
        recent = lessons[-MAX_LESSONS_IN_PROMPT:]
        notes = "\n".join(f"- {l['lesson']}" for l in recent)
        prompt += f"\n\nLessons learned from past attempts (apply them):\n{notes}"
    return prompt


def attempt(task: str, lessons: list[dict]) -> tuple[str, list]:
    messages = [{"role": "user", "content": task}]
    system = build_system_prompt(lessons)

    for _ in range(MAX_STEPS):
        response = client.messages.create(
            model=MODEL, max_tokens=2000, system=system, tools=TOOLS, messages=messages
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            final = "".join(b.text for b in response.content if b.type == "text")
            return final, messages

        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = run_python(block.input["code"])
                print(f"  [tool] ran code -> {output[:100]!r}")
                results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": output}
                )
        messages.append({"role": "user", "content": results})

    return "Stopped: hit the step limit.", messages


# ---------- Reflection ----------
def reflect(task: str, final: str, messages: list) -> dict:
    transcript = json.dumps(
        [
            {"role": m["role"], "content": m["content"] if isinstance(m["content"], str) else str(m["content"])}
            for m in messages
        ]
    )[:8000]
    prompt = (
        f"Task: {task}\n\nTranscript: {transcript}\n\nFinal answer: {final}\n\n"
        "Review this attempt. Reply with ONLY JSON: "
        '{"success": true/false, "lesson": "one short, general, reusable lesson"}'
    )
    response = client.messages.create(
        model=MODEL, max_tokens=300, messages=[{"role": "user", "content": prompt}]
    )
    text = response.content[0].text.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"success": False, "lesson": ""}


# ---------- Main ----------
def run_task(task: str) -> None:
    lessons = load_lessons()
    print(f"\nTask: {task}\n(using {len(lessons)} stored lessons)")
    final, messages = attempt(task, lessons)
    print(f"Answer: {final}")

    review = reflect(task, final, messages)
    print(f"Self-review: success={review['success']} | lesson={review['lesson']!r}")
    if review.get("lesson"):
        save_lesson(task, review["lesson"])


if __name__ == "__main__":
    tasks = sys.argv[1:] or [
        "Write a function that returns the n-th Fibonacci number and test it for n=0, 1, 10.",
        "Write a function that checks whether a string is a valid palindrome, ignoring punctuation and case. Test it.",
    ]
    for t in tasks:
        run_task(t)
