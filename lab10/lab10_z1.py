# Skrypt pobiera od użytkownika zbiór imion, w tym celu:
# pyta o liczbę elementów zbioru,
# pobrać kolejne elementy i zapisać je do listy,
# wyświetla w podsumowaniu, jakie imiona pobrał od użytkownika.

amount = int(input("Podaj liczbę zbioru imion: "))
names = []

for i in range(0, amount):
    name = input("Podaj imię: ")
    names.append(name)

print("Zapisane imiona to:", names)
