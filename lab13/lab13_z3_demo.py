# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta", w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl, jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także większą liczbę liter.

import random


def draw_letter():
    return chr(random.randint(ord("A"), ord("E")))


def draw_row():
    return [draw_letter() for i in range(3)]


def check(row):
    if row[0] == row[1] == row[2]:
        return True
    else:
        return False


counter = 1

while counter:
    row = draw_row()
    print(row, counter)
    if check(row):
        counter = 0
    else:
        counter += 1

'''
Korzystamy z:
print(ord("A"))
print(ord("E"))

print(chr(65))
print(chr(69))
'''
