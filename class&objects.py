"""
class ClassName:
    statements1
    statement2
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point(1, 3, 0)
print(p1.x)
print(p1.y)
print(p1.z)


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a


p1 = Person("Priti", 21)
p2 = Person("Sweety", 23)
print(p1.name, " is ", p1.age, " years old.")
print(p2.name, " is ", p2.age, " years old.")



import math
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        a = math.pi * self.radius * self.radius
        return a

    def peri(self):
        p = 2 * math.pi * self.radius
        return p


c1 = Circle(3)
a1 = c1.area()
p1 = c1.peri()
print(a1)
print(p1)
