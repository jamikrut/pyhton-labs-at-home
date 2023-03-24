# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def list_to_tuple(myList1, myList2, myList3):
    myList = myList1 + myList2 + myList3

    myListUnique = []
    for element in myList:
        if element not in myListUnique:
            myListUnique.append(element)

    myTuple = tuple(myListUnique.copy())

    return myTuple


print(list_to_tuple([1, 2], [1, 1], [4, 4, 4]))
