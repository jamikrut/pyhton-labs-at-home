# Skrypt wyświetla liczby od 1 do 100 z pominięciem liczb podzielnych przez 3.

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i, end=" ")

# to samo rozpisane czytelniej
print("")

for i in range(1, 101):
    if i % 3 == 0:
        continue
    else:
        print(i, end=" ")

# Inny sposób
print("")

for i in range(1, 101):
    if i % 3 != 0:
        print(i, end=" ")
