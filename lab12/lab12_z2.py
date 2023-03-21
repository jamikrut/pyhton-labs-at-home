# Skrypt oblicza obwód, pole powierzchni i długość przekątnej dla prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998.


def rectangleSurfaceArea(a, b):  # pole
    return "Pole prostokąta o bokach " + str(a) + " i " + str(b) + " wynosi " + str(a * b) + "."


def rectanglePerimeter(a, b):  # obwód
    return "Obwód prostokąta o bokach " + str(a) + " i " + str(b) + " wynosi " + str(2 * (a + b)) + "."


def rectangleDiagonal(a, b):  # przekątna
    return "Przekątna prostokąta o bokach " + str(a) + " i " + str(b) + " wynosi " + str((a ** 2 + b ** 2) ** 0.5) + "."


print(rectangleSurfaceArea(4, 5))
print(rectanglePerimeter(4, 5))
print(rectangleDiagonal(4, 5))

print()
print(rectangleSurfaceArea(2678, 5678))
print(rectanglePerimeter(2678, 5678))
print(rectangleDiagonal(2678, 5678))

print()
print(rectangleSurfaceArea(344555, 788998))
print(rectanglePerimeter(344555, 788998))
print(rectangleDiagonal(344555, 788998))
