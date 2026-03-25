grades = [
    [70, 85, 90],
    [100, 90],
    [60, 74, 80, 90]
]

averages = []

for i in range(len(grades)):
    total = 0
    count = 0
    for j in range(len(grades[i])):
        total += grades[i][j]
        count += 1
    avg = total / count
    averages.append(avg)

print("Averages:", averages)