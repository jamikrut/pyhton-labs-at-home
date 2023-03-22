# Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

def uniqueElementList(inputList):
    modifiedList = []
    for i in range(len(inputList)):
        if inputList[i] not in modifiedList:
            modifiedList.append(inputList[i])
    return modifiedList


myList = [2, 3, 2, 5, 1, 2, 4, 2, 6]
print(uniqueElementList(myList))
