# Skrypt wyznacza wartość n-tego bitu dla dowolnej liczby całkowitej.
# Bity liczymy od 0, od najmniej znaczącego bitu.

number = int(input("Podaj liczbę całkowitą: "))
bit_nr = int(input("Który bit chcesz wyświetlić?: "))
print("Liczbę " + str(number) + " zapiszemy jako " + "{:08b}".format(number))
print(str(bit_nr) + " bit tej cyfry to ", end="")
print(("{:08b}".format(number >> bit_nr))[-1])
