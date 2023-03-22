# !!!!!!!! skrypt nie skończony - metoda 1 sotrowanie moje (mind append)

# Napisz skrypt pobierający od użytkownika serię liczb całkowitych,
# a następnie wyświetla je w kolejności malejącej, pozbywając się wcześniej duplikatów.

seriesRange = int(input("Podaj długość serii liczb: "))
inputSeries = []

print("Podaj teraz kolejno liczby do serii liczb:")
for i in range(seriesRange):
    inputSeries.append(int(input()))

print("Podana przez Ciebie seria liczb to:", inputSeries)

loopContinue = 1
sortedSeries = []

for i in range(len(inputSeries)):
    minNumber = inputSeries[0]
    for j in range(len(inputSeries) - i):
        if inputSeries[j] < minNumber:
            minNumber = inputSeries[j]
    if minNumber not in sortedSeries:
        sortedSeries.append(minNumber)

print("Oto uporządkowana, podana przez Ciebie seria licz:", sortedSeries)
