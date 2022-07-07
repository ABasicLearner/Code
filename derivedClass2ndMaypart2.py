""" WAP to create a class "shape" and define property - height
 Then derive two classses - 1) triangle (height and base)
                            2) Rectangle (height and width)
 Write area and perimeter method for triangle as well as rectangle
"""


class Shape:
    def __init__(self, height):
        self.h = height
# if we define methods in this base class then it is available for each child class or derived class

class Triangle(Shape):
    def __init__(self, height, basewidth):
        super(Triangle, self).__init__(height)        # study its exact use
        self.b = basewidth

    def area(self):
        a = self.b * self.h / 2
        return a


class Rectangle(Shape):
    def __init__(self, height, width):
        super(Rectangle, self).__init__(height)
        self.w = width

    def area(self):
        a = self.w * self.h
        return a

    def perimeter(self):
        p = 2 * (self.h + self.w)
        return p


t = Triangle(2, 4)
r = Rectangle(2, 4)
print("Area of triangle is: ", t.area())
print("Area of rectangle is: ", r.area())
print("Perimeter of rectangle is: ", r.perimeter())

# cpp (book) by Kanetkar


