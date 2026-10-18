#numbers = [33, 34, 55, 24, 82,
 #          6, 15, 18, 5, 22,
  #         25, 35, 20, 24, 17]

#frequency = {}

#for number in numbers:
#    if number in frequency:
 #       frequency[number] += 1
  #  else:
   #     frequency[number] = 1

#print(frequency)

"""data = data = [
    [33, 34, 55, 24, 82],
    [6, 15, 18, 5, 22],
    [25, 35, 20, 24, 17],
    [4, 61, 19, 69, 74],
    [55, 24, 26, 13, 63],
    [30, 68, 25, 24, 76],
    [36, 34, 13, 22, 18],
    [78, 63, 72, 31, 37],
    [81, 86, 63, 17, 3],
    [51, 7, 88, 50, 15],
    [29, 9, 8, 18, 20],
    [4, 61, 40, 6, 74],
    [83, 84, 74, 9, 8],
    [23, 89, 44, 68, 61],
    [37, 1, 19, 35, 10],
    [38, 19, 51, 86, 15],
    [33, 14, 70, 18, 75],
    [20, 30, 33, 4, 65],
    [18, 3, 24, 36, 35],
    [78, 24, 9, 50, 56],
    [47, 12, 69, 60, 80],
    [6, 58, 62, 4, 20],
    [31, 26, 1, 19, 6],
    [16, 11, 4, 33, 48],
    [30, 58, 73, 83, 38],
    [76, 38, 44, 55, 12],
    [52, 53, 12, 1, 17],
    [27, 13, 8, 25, 5],
    [10, 74, 70, 62, 49],
    [51, 26, 75, 17, 43],
    [85, 42, 45, 23, 15],
    [5, 36, 38, 6, 32],
    [60, 2, 34, 8, 54],
    [35, 40, 84, 14, 13],
    [3, 10, 8, 37, 81],
    [27, 37, 9, 19, 5],
    [28, 6, 21, 59, 4],
    [47, 78, 48, 22, 73],
    [48, 71, 47, 9, 50],
    [23, 31, 29, 34, 27],
    [13, 76, 1, 11, 81]
]

numbers = []

for row in data:
    for number in row:
        numbers.append(number)

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)
sorted_frequency = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

print(sorted_frequency)

last_seen = {}

for i, row in enumerate(data):
    for number in row:
        last_seen[number] = i

total_draws = len(data)

for number in frequency:
    gap = total_draws - 1 - last_seen[number]
    print(f"Number {number}: appeared {frequency[number]} times, gap = {gap}")

scores = {}

for number in frequency:
    freq = frequency[number]
    gap = total_draws - 1 - last_seen[number]

    score = freq * 2 + gap * 0.5

    scores[number] = score

sorted_scores = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\n--- PREDICTION SCORES ---")

for number, score in sorted_scores:
    print(f"Number {number}: {score:.2f}") """

"""data = [
    [33, 34, 55, 24, 82],
    [6, 15, 18, 5, 22],
    [25, 35, 20, 24, 17],
    [4, 61, 19, 69, 74],
    [55, 24, 26, 13, 63],
    [30, 68, 25, 24, 76],
    [36, 34, 13, 22, 18],
    [78, 63, 72, 31, 37],
    [81, 86, 63, 17, 3],
    [51, 7, 88, 50, 15],
    [29, 9, 8, 18, 20],
    [4, 61, 40, 6, 74],
    [83, 84, 74, 9, 8],
    [23, 89, 44, 68, 61],
    [37, 1, 19, 35, 10],
    [38, 19, 51, 86, 15],
    [33, 14, 70, 18, 75],
    [20, 30, 33, 4, 65],
    [18, 3, 24, 36, 35],
    [78, 24, 9, 50, 56],
    [47, 12, 69, 60, 80],
    [6, 58, 62, 4, 20],
    [31, 26, 1, 19, 6],
    [16, 11, 4, 33, 48],
    [30, 58, 73, 83, 38],
    [76, 38, 44, 55, 12],
    [52, 53, 12, 1, 17],
    [27, 13, 8, 25, 5],
    [10, 74, 70, 62, 49],
    [51, 26, 75, 17, 43],
    [85, 42, 45, 23, 15],
    [5, 36, 38, 6, 32],
    [60, 2, 34, 8, 54],
    [35, 40, 84, 14, 13],
    [3, 10, 8, 37, 81],
    [27, 37, 9, 19, 5],
    [28, 6, 21, 59, 4],
    [47, 78, 48, 22, 73],
    [48, 71, 47, 9, 50],
    [23, 31, 29, 34, 27],
    [13, 76, 1, 11, 81]
]


# -------------------------
# STEP 1: Count frequency
# -------------------------

frequency = {}

for row in data:
    for number in row:

        if number not in frequency:
            frequency[number] = 0

        frequency[number] += 1


# -------------------------
# STEP 2: Find last appearance
# -------------------------

last_seen = {}

for draw_number, row in enumerate(data):

    for number in row:
        last_seen[number] = draw_number


# -------------------------
# STEP 3: Calculate scores
# -------------------------

total_draws = len(data)

scores = {}

for number in frequency:

    freq = frequency[number]

    gap = total_draws - 1 - last_seen[number]

    score = (freq * 2) + (gap * 0.5)

    scores[number] = score


# -------------------------
# STEP 4: Sort scores
# -------------------------

sorted_scores = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)


# -------------------------
# STEP 5: Show prediction
# -------------------------

print("\n===== TOP 5 PREDICTION =====")

for number, score in sorted_scores[:5]:

    print(
        f"Number {number} | "
        f"Frequency: {frequency[number]} | "
        f"Gap: {total_draws - 1 - last_seen[number]} | "
        f"Score: {score:.2f}"
    )"""

# Your data stays exactly the same
data = [
    [33, 34, 55, 24, 82],
    [6, 15, 18, 5, 22],
    [25, 35, 20, 24, 17],
    [4, 61, 19, 69, 74],
    [55, 24, 26, 13, 63],
    [30, 68, 25, 24, 76],
    [36, 34, 13, 22, 18],
    [78, 63, 72, 31, 37],
    [81, 86, 63, 17, 3],
    [51, 7, 88, 50, 15],
    [29, 9, 8, 18, 20],
    [4, 61, 40, 6, 74],
    [83, 84, 74, 9, 8],
    [23, 89, 44, 68, 61],
    [37, 1, 19, 35, 10],
    [38, 19, 51, 86, 15],
    [33, 14, 70, 18, 75],
    [20, 30, 33, 4, 65],
    [18, 3, 24, 36, 35],
    [78, 24, 9, 50, 56],
    [47, 12, 69, 60, 80],
    [6, 58, 62, 4, 20],
    [31, 26, 1, 19, 6],
    [16, 11, 4, 33, 48],
    [30, 58, 73, 83, 38],
    [76, 38, 44, 55, 12],
    [52, 53, 12, 1, 17],
    [27, 13, 8, 25, 5],
    [10, 74, 70, 62, 49],
    [51, 26, 75, 17, 43],
    [85, 42, 45, 23, 15],
    [5, 36, 38, 6, 32],
    [60, 2, 34, 8, 54],
    [35, 40, 84, 14, 13],
    [3, 10, 8, 37, 81],
    [27, 37, 9, 19, 5],
    [28, 6, 21, 59, 4],
    [47, 78, 48, 22, 73],
    [48, 71, 47, 9, 50],
    [23, 31, 29, 34, 27],
    [13, 76, 1, 11, 81]
]


def predict(training_data, freq_weight, gap_weight):

    frequency = {}
    last_seen = {}

    for draw_number, row in enumerate(training_data):

        for number in row:

            if number not in frequency:
                frequency[number] = 0

            frequency[number] += 1
            last_seen[number] = draw_number

    total_draws = len(training_data)

    scores = {}

    for number in frequency:

        freq = frequency[number]

        gap = total_draws - 1 - last_seen[number]

        score = (freq * freq_weight) + (gap * gap_weight)

        scores[number] = score

    sorted_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [number for number, score in sorted_scores[:5]]


# --------------------------------
# BACKTEST
# --------------------------------

total_correct = 0
tests = 0

for i in range(20, len(data)):

    training_data = data[:i]

    actual_result = data[i]

    prediction = predict(training_data)

    correct = set(prediction) & set(actual_result)

    print("\nTest", tests + 1)
    print("Prediction:", prediction)
    print("Actual:    ", actual_result)
    print("Correct:   ", list(correct))

    total_correct += len(correct)
    tests += 1


# --------------------------------
# FINAL RESULT
# --------------------------------

average = total_correct / tests

print("\n==========================")
print("BACKTEST COMPLETE")
print("==========================")

print("Tests:", tests)
print("Total correct:", total_correct)
print("Average correct:", round(average, 2))

best_average = 0
best_weights = None

for freq_weight in [1, 2, 3, 4, 5]:

    for gap_weight in [0, 0.05, 0.1, 0.15, 0.2, 0.25]:

        total_correct = 0
        tests = 0

        for i in range(20, len(data)):

            training_data = data[:i]

            actual = data[i]

            prediction = predict(
                training_data,
                freq_weight,
                gap_weight
            )

            correct = set(prediction) & set(actual)

            total_correct += len(correct)

            tests += 1

        average = total_correct / tests

        if average > best_average:

            best_average = average

            best_weights = (
                freq_weight,
                gap_weight
            )


print("\n==========================")
print("BEST MODEL")
print("==========================")

print("Frequency weight:", best_weights[0])
print("Gap weight:", best_weights[1])
print("Average correct:", round(best_average, 2))