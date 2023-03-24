# Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy
# wyższy poziom wymaga jednej puszki mniej niż poziom na którym go
# zbudowano. Korzystając z rekurencji napisz program, który pozwoli
# wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym
# poziomie oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z
# dostępnej liczby puszek. Przykład: jeżeli chcemy ułożyć 3 poziomową
# wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4 poziomową wieżę.

def how_many_tins_needed(levels):
    if levels < 1:
        return "Niepoprawna ilość poziomów!"
    if levels < 2:
        return 1
    if levels < 3:
        return 3
    return how_many_tins_needed(levels - 1) + levels


for i in range(11):
    print(i, "potrzeba", how_many_tins_needed(i))


def how_many_levels_build(tins):
    if tins < 1:
        return "Niepoprawna ilość puszek!"
    if tins < how_many_tins_needed(2):  # 3 puszki
        return 1
    if tins < how_many_tins_needed(3):  # 6 puszek
        return 2
    if tins < how_many_tins_needed(2 + how_many_levels_build(tins - 1)):
        return how_many_levels_build(tins - 1) + 1
    else:
        return how_many_tins_needed(tins - 1)


for i in range(11):
    print(i, "daje", how_many_levels_build(i))
