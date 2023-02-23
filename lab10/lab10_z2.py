# Skrypt symuluje 16 rzutów kostką do gry, a następnie wyświetla poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

import random

throwResults = []

for i in range(0, 16):
    throw = random.randint(1, 6)
    throwResults.append(throw)

print("Zestaw wylosowanych wyników, to:", throwResults)
print("Za 8 razem padła wartość", str(throwResults[7]) + ".")

counter = 0
for i in range(0, 16):
    if throwResults[i] == 6:
        counter += 1
print("6 wypdała", counter, "razy.")

inRowCount = 1
maxInRow = 1
counter = 1

for i in range(1, 16):
    if throwResults[i] == throwResults[i - 1]:
        counter += 1
        if counter > maxInRow:
            maxInRow = counter
    else:
        counter = 1
print("Maksymalna liczba wyrzuconych tych samych wartości pod rząd to " + str(maxInRow) + ".")
