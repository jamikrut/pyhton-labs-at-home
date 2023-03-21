# Napisz skrypt pobierający od użytkownika serię liczb całkowitych,
# a następnie wyświetla je w kolejności malejącej, pozbywając się wcześniej duplikatów.

# metoda 3 - najprosztsza - użycie metody sort()

seriesRange = int(input("Podaj długość serii liczb: "))
inputSeries = []

print("Podaj teraz kolejno liczby do serii liczb:")
for i in range(seriesRange):
    inputSeries.append(int(input()))

print("Podana przez Ciebie seria liczb to:", inputSeries)

loopContinue = 1
sortedSeries = inputSeries[:]

sortedSeries.sort()
sortedSeriesUnique = []

for i in range(len(sortedSeries)):
    if sortedSeries[i] not in sortedSeriesUnique:
        sortedSeriesUnique.append(sortedSeries[i])

print("Oto uporządkowana, podana przez Ciebie seria liczb bez powtórzeń:", sortedSeriesUnique)
