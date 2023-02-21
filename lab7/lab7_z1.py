# Skrypt sprawdza czy pierwiastek kwadratowy z liczby całkowitej pobranej od użytkownika
# jest także liczbą całkowitą.

number = int(input("Podaj liczbę całkowitą: "))
numberSqrt = number ** 0.5

print("Pierwiastek z liczby " + str(number), end=" ")
if numberSqrt == numberSqrt // 1:
    print("jest liczbą całkowitą", end=" ")
else:
    print("nie jest liczbą całkowitą", end=" ")
print("i wynosi " + str(numberSqrt) + ".")
