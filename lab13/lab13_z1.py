# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

def elementsToPower(myList, power):
    return [i ** power for i in myList]


myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(elementsToPower(myList, 3))
