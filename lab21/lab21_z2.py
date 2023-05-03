class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val

    def show(self):
        print(self.stack_list)


stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

for i in range(1, 101):
    stack1.push(i)

for i in range(100):
    stack2.push(stack1.pop())

for i in range(100):
    stack3.push(stack2.pop())

for i in range(100):
    if i > 98:
        print(stack3.pop(), end="")
        continue
    print(stack3.pop(), end=", ")
