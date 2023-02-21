# Skrypt rysuje na ekranie prostokąt zbudowany ze znaku jak i wymiarów określonych przez użytkownika

char = input("Podaj znak: ")
columns = int(input("Podaj liczbę kolumn: "))
rows = int(input("Podaj liczbę wierszy: "))
print((char * columns + '\n') * rows, end="")
