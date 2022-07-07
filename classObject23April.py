# read about static variable

# Write a python class named rectangle
"""class Rectangle:
    def __init__(self, length, width):
        self.len = length
        self.wid = width

    def area(self):
        a = self.len * self.wid
        return a

    def peri(self):
        p = 2 * (self.len + self.wid)
        return p


r = Rectangle(4, 5)
a1 = r.area()
p1 = r.peri()
print(a1)
print(p1)
"""

"""
class Student:
    def __init__(self, rollnumber, name, classname, sub1, sub2, sub3):
        self.r = rollnumber
        self.n = name
        self.c = classname
        self.mark = [sub1, sub2, sub3]

    def percent(self):
        p = (self.mark[0] + self.mark[1] + self.mark[2]) / 3
        return p


list1 = [Student(1, "A", "FY", 44, 58, 64), Student(2, "B", "FY", 78, 78, 78), Student(3, "C", "FY", 84, 78, 94),
         Student(4, "D", "FY", 64, 70, 59), Student(5, "E", "FY", 68, 72, 68)]
perc = [list1[0].percent(), list1[1].percent(), list1[2].percent(), list1[3].percent(), list1[4].percent()]
mini = []
for i in perc:
    for j in range(i+1, 5):
        if perc[i] < perc[j]:
            mini[i] = perc[i]
            perc[i] = perc[j]
            perc[j] = mini[i]
for i in mini:
    """

class Student:
    def __init__(self, rollnumber, name, classname, sub1, sub2, sub3):
        self.r = rollnumber
        self.n = name
        self.c = classname
        self.mark = [sub1, sub2, sub3]

    def percent(self):
        p = (self.mark[0] + self.mark[1] + self.mark[2]) / 3
        return p

    def showresult(self):
        print("")


s1 = Student(1, "A", "FY", 44, 58, 64)
s2 = Student(2, "B", "FY", 78, 78, 78)
s3 = Student(3, "C", "FY", 84, 78, 94)

p1 = s1.percent()
p2 = s2.percent()
p3 = s3.percent()
p = list[p1, p2, p3]
p.sort()
