# Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez użytkownika,
# • wyświetli wylosowane serie liczb.

print("Program losuje kilka serii liczb całkowitych, według wybranego przez Ciebie kryterium.")

print("\nWybierzemy teraz zakres cyfr do losowania.")
minDigit = int(input("Podaj zakres cyfr od: "))
maxDigit = int(input("Podaj zakres cyfr do: "))

print("\nWybierzemy teraz ilość cyfr do losowania z wybranego zakresu.")
minDigitsAmount = int(input("Ilość losowania cyfr od: "))
maxDigitsAmount = int(input("Ilość losowania cyfr do: "))

print("\nWybierzemy ilość takich serii do wylosowania.")
minSeries = int(input("Zakres serii od: "))
maxSeries = int(input("Zakres serii do: "))
print("")

import random

digitsAmount = random.randint(minDigitsAmount, maxDigitsAmount)
seriesNumber = random.randint(minSeries, maxSeries)

for i in range(0, seriesNumber):
    digitList = []

    for j in range(0, digitsAmount):
        digit = random.randint(minDigit, maxDigit)
        digitList.append(digit)

    print("Wylosowane cyfry dla serii", str(i + 1), "to:", digitList)
