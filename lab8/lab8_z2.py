# Skrypt wyświetla na ekranie macierz.
# Rozmiar macierzy oraz znak, z jakiej będzie zbudowana, określa użytkownik.

size = int(input("Podaj rozmiar: "))
char = input("Podaj znak: ")

for i in range(0, size):
    print(char * size)
