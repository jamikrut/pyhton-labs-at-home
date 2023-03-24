phones = {
    "Adam": 123432546,
    "Karol": 759375940,
    "Mariola": 683629052,
    "Iza": 749720924
}

while True:
    name = input("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("Numer telefonu dla", name, "to:", phones[name])
    else:
        print("Nie znaleziono telefonu dla", name)
