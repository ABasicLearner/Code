# 1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are!"
      "\n\t\tUp above the world so high, \n\t\tlike a diamond in the sky."
      "\nTwinkle, twinkle, little star,"
      "\n\tHow I wonder what you are")

# 2
import datetime as dt
current = dt.datetime.now()
print("Current date and time: ")
print(current.strftime("%Y-%m-%d %H:%M:%S"))

# 3
radius = input("Enter radius to get area of circle: ")
r = int(radius)
area = 3.142 * r * r
print(area)

# 4
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(lname + " " + fname)

# 5
n = int(input("How many terms in Fibonacci sequence?: "))
n1, n2 = 0, 1
if n == 1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)

# 6
str = input("Enter a sequence of numbers in comma separated manner: ")
list1 = str.split(",")
tuple1 = tuple(list1)
print("List: ", list1)
print("Tuple: ", tuple1)

# 7
filename = input("Enter a file name with extension: ")
file_ext = filename.split(".")
print("The extension of the file is: " + str(file_ext[-1]))

# 8
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[-1])

# 9
start_date = (11, 12, 2014)
print("The exams will start from: %i / %i / %i" % start_date)

# 10
n = int(input("Enter a number: "))
n1.str(n)
sum = 0
sum = int(n1) + int(n1*2) + int(n1*3)
print(sum)


# **************************
n = int(input("Enter an integer: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print(n1 + n2 + n3)

# 11
print(abs.__doc__)
print("abs(-120):", abs(-120))

# 12
import builtins
help(builtins.abs)
print("abs(-120):", builtins.abs(-120))

# 13
import calendar
y = int(input("Enter year: "))
m = int(input("Enter month: "))
print(calendar.month(y, m))

# 14
from datetime import date
fdate = date(2014, 7, 2)
ldate = date(2014, 7, 11)
diff = ldate - fdate
print(diff.days, "days")
