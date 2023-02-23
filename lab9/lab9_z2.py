# Skrypt udowadnia, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są parzyste i jednocześnie większe od 90,
# a gdy są nieparzyste, to przynajmniej dzielą się przez 9.

count = 0
numbers = ""

for i in range(1, 101):
    if (i % 2 == 0) and (i > 90):
        count += 1
        if count == 1:
            numbers = str(i)
        else:
            numbers = numbers + ", " + str(i)
    elif (i % 2 != 0) and (i % 9 == 0):
        count += 1
        if count == 1:
            numbers = str(i)
        else:
            numbers = numbers + ", " + str(i)

print("Jest", str(count), "takich cyfr.")
print("Te cyfry to: ", numbers, ".", sep="")
