# Homework -> find function/way to call the method using class name
"""class Temperature:
    def __init__(self, celsius, fahrenheit):
        self.cel = celsius
        self.fah = fahrenheit

    def convert_to_celsius(self):
        celsius = (self.cel - 32) * 5 / 9
        return celsius

    def convert_to_fahrenheit(self):
        fahrenheit = (self.cel * 9 / 5) + 32
        return fahrenheit


temp = Temperature(34, 273)
t1 = temp.convert_to_fahrenheit()
t2 = temp.convert_to_celsius()
print(t1)
print(t2)

print()
print()
"""

class Student:
    def __init__(self, name, rollnumber):
        self.n = name
        self.r = rollnumber

    def display(self):
        return self.n, self.r



