class Parent:

    def __init__(self, s):
        self.surname = s
    def showSurName(self):
        print("base : ", self.surname)

class DerivedClass(Parent):
    def __init__(self, n, s):
        super(DerivedClass, self).__init__(s)
        self.name = n
    def showName(self):
        print(self.name)

d = DerivedClass("Ganesh", "Pitale")
# d.surname = "Pitale"
print(d.name, d.surname)
d.showSurName()
d.showName()

p = Parent("Salunkhe")
p.showSurName()
