# Skrypt zawiera funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną ilość razy, w poziomie lub w pionie.

def printChar(char, horizontal, vertical):
    print((str(char) * horizontal + "\n") * vertical, end="")


printChar("#", 21, 9)
