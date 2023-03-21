# Skrypt symuluje grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.

import random

lotteryNumbers = []
counter = 6

while counter:
    number = random.randint(1, 49)
    if number not in lotteryNumbers:
        lotteryNumbers.append(number)
        counter -= 1

print("Obstaw 6 liczb z zakresu 1 do 49:")

betNumbers = []
for i in range(6):
    betNumbers.append(int(input()))

userHit = 0

for i in range(len(betNumbers)):
    if betNumbers[i] in lotteryNumbers:
        userHit += 1

print("W losowaniu padły liczby:", lotteryNumbers)
print("Trafiłeś", userHit, "liczb.")
