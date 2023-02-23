# Skrypt znajduje najczęściej występującą cyfrę w zbiorze.
# Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4, występuje 3 razy.

numbersSet = [4, 1, 2, 9, 4, 4]
print("Podany zbiór: ", numbersSet)

maxOccurrences = []
for i in range(0, len(numbersSet)):
    number = numbersSet[i]
    counter = 0
    for j in range(0, len(numbersSet)):
        if number == numbersSet[j]:
            counter += 1
    maxOccurrences.append(counter)

maxOccNumber = 0
for k in range(0, len(maxOccurrences)):
    if maxOccurrences[k] > maxOccNumber:
        maxOccNumber = numbersSet[k]

print("W zbiorze najczęściej wystąpiła cyfra:", maxOccNumber)
