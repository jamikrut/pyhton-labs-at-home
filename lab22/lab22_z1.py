class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname + " " + self.__lastname

    def getage(self):
        return self.__age

    def risesalary(self, rise_percent=10):
        self.__salary *= (1 + rise_percent / 100)
        return self.__salary


employee = []
employee.append(Employee("Jan", "Kowalski", 25, 3800))
employee.append(Employee("Edmund", "Kaczmarczyk", 45, 7100))
employee.append(Employee("Natalia", "Nowak", 60, 15200))

print("Lista płac")
print("-" * 50)

print("Pierwotna pensja:")
for e in employee:
    print(e.getfullname(), "wiek:", e.getage(), "lat,", "pensja:", e.getsalary(), "zł")

print("\nPensja po podwyżce:")
for e in employee:
    print(e.getfullname(), "wiek:", e.getage(), "lat,", "pensja:", round(e.risesalary(10), 2), "zł")
