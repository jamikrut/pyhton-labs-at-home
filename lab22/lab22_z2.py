class MyClass:
    counter = 0

    def __init__(self):
        MyClass.counter += 1

    def how_many_instances(self):
        return MyClass.counter


instance1 = MyClass()
instance2 = MyClass()
instance3 = MyClass()
instance4 = MyClass()
instance5 = MyClass()
instance6 = MyClass()
instance7 = MyClass()

print("Liczba instancji:", instance1.how_many_instances())
