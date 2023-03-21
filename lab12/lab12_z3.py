# Skrypt zawiera program obliczający wskaźnik BMI (Body Mass Index), w tym celu:
# • zapyta użytkownika o wzrost i wagę,
# • tworzy funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • tworzy funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga, otyłość) na podstawie wskaźnika BMI,
# • prezentuje wyniki korzystając z wcześniej przygotowanych funkcji.

def BMI(height_cm, weight_kg):
    BMI_Index = weight_kg / (height_cm / 100) ** 2
    return BMI_Index


def BMI_Interpreter(BMI):
    if BMI >= 30:
        return ", jesteś otyły!"
    elif BMI >= 25:
        return ", masz nadwagę."
    elif BMI >= 18.5:
        return ", twoja waga jest optymalna."
    elif BMI > 0:
        return ", masz niedowagę!"
    else:
        return ", nieprawidłowe BMI!"


print("Twoje BMI wynosi", BMI(204, 94), BMI_Interpreter(BMI(204, 94)))
