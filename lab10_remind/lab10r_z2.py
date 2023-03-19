# Napisz program, który zasymuluje 16 rzutów kostką do gry, a następnie wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

import random

resultsList = []

for i in range(16):
    resultsList.append(random.randint(1, 6))

print("Zestaw wylosowanych wyników:", resultsList)
print("Za 8 razem padł wynik:", resultsList[7])

counter = 0
for i in range(len(resultsList)):
    if resultsList[i] == 6:
        counter += 1

print("Wynik 6 został otrzymany", counter, "razy.")

counter = 1
resultsInRow = 1

for i in range(1, len(resultsList)):
    if resultsList[i] == resultsList[i - 1]:
        counter += 1
        if resultsInRow < counter:
            resultsInRow = counter
    else:
        counter = 1

print("Ta sama wartość pod rząd padła maksymalnie", resultsInRow, "razy.")
