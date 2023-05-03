class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("Cześć, jestem", self.__name, "i mam", str(self.__age), "lat/a.")


persons = []

persons.append(Person("Janek", 20))
persons.append(Person("Franek", 52))
persons.append(Person("Sara", 35))
persons.append(Person("Julia", 30))
persons.append(Person("Leon", 37))

for person in persons:
    person.introduce()
