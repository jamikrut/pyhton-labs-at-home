# Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
# Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4, występuje 3 razy.

numberSet = [4, 1, 2, 9, 4, 4]
numbersOccurred = []

for i in range(1, 10):
    counter = 0
    for j in range(len(numberSet)):
        if i == numberSet[j]:
            counter += 1
    numbersOccurred.append(counter)

maxTimesOccurred = 0
digitValue = 0
for i in range(len(numbersOccurred)):
    if numbersOccurred[i] > maxTimesOccurred:
        maxTimesOccurred = numbersOccurred[i]
        digitValue = i + 1

print("W zbiorze", numberSet, "najczęściej wystąpiła cyfra", digitValue, "która wystąpiła", maxTimesOccurred, "razy.")
