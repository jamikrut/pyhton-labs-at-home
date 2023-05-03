from lab21_z2 import Stack


class StackExtended(Stack):
    def __init__(self):
        Stack.__init__(self)

    def empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack_list)

    def top(self):
        if not self.empty():
            return self.stack_list[-1]
        return None


print("\n")

stack = StackExtended()
print("Czy stos jest pusty?", stack.empty())
print("Co znajduje się  na górze stosu?", stack.top())

print()
print("Wrzucamy elementy do stosu...")
stack.push("element1")
stack.push("element2")
stack.push("element3")
print()

print("Czy stos jest pusty?", stack.empty())
print("Ile elementów jest na stosie?", stack.size())
print("Co znajduje się  na górze stosu?", stack.top())
