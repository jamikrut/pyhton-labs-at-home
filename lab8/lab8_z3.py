'''
Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
więcej ziaren niż na pole poprzednie. Skrypt zasymuluje
taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.
'''

amount = 1
total = 1

for i in range(1, 8 ** 2):
    amount *= 2
    total = total + amount
print("Suma wszytskich ziaren to ", str(total), ".", sep="")
