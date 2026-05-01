
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print("add:", self.a + self.b)
    def sub(self):
        print("sub:", self.a - self.b)
    def multi(self):
        print("multi:", self.a * self.b)
    def div(self):
        print("div:", self.a / self.b)
    def modular(self):
        print("modular:", self.a % self.b)
    def squares(self):
        print("square of a:", self.a ** 2)
    def cubes(self):
        print("cube of a:", self.a ** 3)
    def power(self):
        print("power (a^b):", self.a ** self.b)
    def average(self):
        print("average:", (self.a + self.b) / 2)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = Calculator(a, b)
c.add()
c.sub()
c.multi()
c.div()
c.modular()
c.squares()
c.cubes()
c.power()
c.average()