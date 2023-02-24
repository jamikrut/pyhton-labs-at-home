# Napisz program pobierający od użytkownika liczbę całkowitą
# i zwracający # liczbę jedynek w ciągu bitów reprezentujących tę liczbę.

print("Program zwraca liczbę jedynek w ciągu bitów reprezentujących podaną liczbę.")
digit = int(input("Podaj liczbę całkowitą: "))

print("Liczbę " + str(digit) + " zapiszemy jako " + "{:08b}".format(digit))
digitLen = len("{:08b}".format(digit))
counter = 0

for i in range(0, digitLen):
    if int(("{:08b}".format(digit >> i))[-1]) == 1:
        counter += 1

print("W zapisie liczby " + str(digit) + " jedynka występuje " + str(counter) + " razy.")
