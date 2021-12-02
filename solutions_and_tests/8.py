class ExtendedStack(list):
    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a + b)
        # операция сложения

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a - b)
        # операция вычитания

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.append(a * b)
        # операция умножения

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a // b)
        # операция целочисленного деления

lst = ExtendedStack()
lst.append(3)
lst.append(3)
lst.div()
print(lst)