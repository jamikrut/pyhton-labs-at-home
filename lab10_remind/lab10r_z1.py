# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu, jakie imiona pobrał od użytkownika.

namesAmount = int(input("Podaj liczbę imion do pobrania: "))
namesList = []

while namesAmount:
    namesList.append(input("Podaj imię: "))
    namesAmount -= 1
print("Pobrane imiona:", namesList)
