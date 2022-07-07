
"""
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        # to display point as (x,y,z), str converts any character into string
        s = "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
        return s


p1 = Point(2, 5, 8)
print(p1)     # gives memory address in hexadecimal form
newstr = "First point is:  " + str(p1.__str__())
print(newstr)
"""

"""
class Time:
    def __init__(self, hours, minutes):
        self.hr = hours
        self.min = minutes

    def addTime(self, t2):
        tm = self.min + t2.min
        if tm >= 60:
            tm = tm - 60
            h = self.hr + t2.hr + 1
        else:
            h = self.hr + t2.hr
        print(h, tm)


tm1 = Time(2, 59)
tm2 = Time(1, 47)
tm1.addTime(tm2)
"""

"""
class Time:
    def __init__(self, hours, minutes):
        self.hr = hours
        self.min = minutes

    def addTime(self, t):
        m = (self.min + t.min) % 60
        h = (self.hr + t.hr) + (self.min + t.min) // 60
        newTime = Time(h, m)
        return newTime

    def __str__(self):
        return str(self.hr) + "hrs " + str(self.min) + "min"

t1 = Time(2, 57)
t2 = Time(3, 46)
a = t1.addTime(t2)
print(a)
"""


class Time:
    def __init__(self, hours, minutes, seconds = 0):     # seconds = 0 is default parameter
        self.hr = hours
        self.min = minutes
        self.sec = seconds

    def addTime(self, t):
        s = (self.sec + t.sec) % 60
        m = (self.min + t.min) % 60 + ((self.sec + t.sec) // 60)
        h = (self.hr + t.hr) + (self.min + t.min) // 60
        new_time = Time(h, m, s)
        return new_time

    def __str__(self):
        return str(self.hr) + "hrs " + str(self.min) + "min " + str(self.sec) + "sec"


t1 = Time(2, 56)       # even if we do not specify seconds here it'll take 0 sec by default
print(t1)
t2 = Time(3, 126, 40)
print(t2)
time = t1.addTime(t2)
print(time)
