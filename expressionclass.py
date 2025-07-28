class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def addition(self):
        return self.num1 + self.num2 + self.num3
obj = Expression(1,2,3)
print(obj.addition())