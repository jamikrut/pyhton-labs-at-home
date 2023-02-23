# Skrypt wyświetla tylko liczby podzielne przez 3, 5 lub 7,
# ze zbioru liczb z zakresu określonego przez użytkownika.

begin = int(input("Podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))

if end < begin:
    print("Niepoprawny zakres, skrypt zakończył działanie.")
else:
    print("Liczby podzielne przez 3, 5 lub 7 z zakresu od", str(begin), "do", str(end), "to:")
    for i in range(begin, end + 1):
        if (i % 3 == 0) or (1 % 3) == 0 or (1 % 7) == 0:
            print(i, end=" ")
