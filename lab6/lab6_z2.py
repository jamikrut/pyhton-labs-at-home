# Skrypt pobiera od użytkownika dwie liczby całkowite i wykonaj na nich operacje:
# Dodawania, odejmowania, mnożenia, dzielenia oraz operację modulo.
# Rezultaty zostają wyświetlone na ekranie.

a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

print(str(a), "+", str(b), "=", a + b)
print(str(a), "-", str(b), "=", a - b)
print(str(a), "*", str(b), "=", a * b)
print(str(a), "/", str(b), "=", a / b)
print(str(a), "modulo", str(b), "=", a % b)
