# Skrypt zawiera grę w zgadywanie liczby z przedziału od 1 do 10.
# Gracz dostaje 3 szanse.
# Po nieudanej próbie gracz dostaje podpowiedź, np. o parzystości zgadywanej liczby itp.

import random

theNumber = random.randint(1, 10)

userGuess = int(input("Zgadnij, jaką liczbę mam na myśli z przedziału 1 do 10: "))
if userGuess == theNumber:
    print("Brawo! Udało Ci się za pierwszym razem.")
else:
    print("Niestety nie zgadłeś.", end=" ")
    if theNumber % 2 == 0:
        print("Moja liczba jest parzysta.")
    else:
        print("Moja liczba jest nieparzysta.")
    userGuess = int(input("Masz drugą szansę: "))
    if userGuess == theNumber:
        print("Brawo! Udało Ci się za drugim razem.")
    else:
        print("Niestety, znowu nie trafiłeś. Moja liczba jest", end=" ")
        if theNumber > 5:
            print("większa od 5.")
        else:
            print("mniejsza lub równa 5.")
        userGuess = int(input("Masz ostatnią szansę: "))
        if userGuess == theNumber:
            print("Brawo! Do trzech razy sztuka.")
        else:
            print("Przykro mi, nawet teraz nie zgadłeś. Moja liczba to " + str(theNumber) + ".")
