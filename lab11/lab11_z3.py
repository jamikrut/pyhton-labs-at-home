# Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
# • stwórz wirtualną szachownicę,
# • na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
# • zaprezentuj użytkownikowi stan wirtualnej szachownicy.

import random

chessRow = ["__" for i in range(8)]
chessBoard = [chessRow[:] for i in range(8)]

print("Prezentacja pustej szachownicy:")
print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep="     ")
for i in range(len(chessBoard)):
    print(i + 1, "", chessBoard[i])

pawnPosition = []
pawnsCoordinates = []

counter = 0  # liczba pionków do rozstawienia

while counter < 5:
    del pawnPosition[:]
    pawnPosition.append(random.randint(0, 7))
    pawnPosition.append(random.randint(0, 7))
    if pawnPosition not in pawnsCoordinates:
        pawnsCoordinates.append(pawnPosition[:])
    counter = len(pawnsCoordinates)

# print(pawnsCoordinates)

# PW -> pion (pawn)
# QU -> królowa (queen)
# KI - > król (king)
chessBoard[pawnsCoordinates[0][0]][pawnsCoordinates[0][1]] = "PW"
chessBoard[pawnsCoordinates[1][0]][pawnsCoordinates[1][1]] = "PW"
chessBoard[pawnsCoordinates[2][0]][pawnsCoordinates[2][1]] = "PW"
chessBoard[pawnsCoordinates[3][0]][pawnsCoordinates[3][1]] = "QU"
chessBoard[pawnsCoordinates[4][0]][pawnsCoordinates[4][1]] = "KI"

print()
print("Prezentacja zapełnionej szachownicy:")
print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep="     ")
for i in range(len(chessBoard)):
    print(i + 1, "", chessBoard[i])
