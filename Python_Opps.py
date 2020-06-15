class calc:
    def __init__(self,x,y):
        self.arg1 = x
        self.arg2 = y

    def Add(self):
        return (self.arg1 + self.arg2)
    def Substract(self):
        return (self.arg1 - self.arg2)
    def Multiply(self):
        return (self.arg1 * self.arg2)
    def Devision(self):
        return (self.arg1 / self.arg2)

obj1 = calc(9,3)
print(id(obj1))
print(obj1.Add())
print(obj1.Substract())
print(obj1.Multiply())
print(obj1.Devision())

#Objects are Mutable
obj1.arg2 = 10
print(id(obj1))



