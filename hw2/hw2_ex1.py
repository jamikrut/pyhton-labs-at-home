# Skrypt sumuje pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

print("Program sumuje liczby całkowite.")
numbersAmount = int(input("Podaj ilość liczb do zsumowania: "))

numbersSet = []
for i in range(0, numbersAmount):
    number = int(input("Podaj " + str(i + 1) + ". liczbę całkowitą: "))
    numbersSet.append(int(number))

print("Podane liczby to:", numbersSet)

evenSum = 0  # parzyste
oddSum = 0  # nieparzyste

for i in range(0, len(numbersSet)):
    if numbersSet[i] % 2 == 0:
        evenSum += numbersSet[i]
    else:
        oddSum += numbersSet[i]

print("Suma liczb parzystych to", evenSum)
print("Suma liczb nieparzystych to", oddSum)
