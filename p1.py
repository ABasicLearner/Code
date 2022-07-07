# Write a Python program to find the maximum of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print(a, " is the greatest")
    else:
        print(c, " is the greatest")
elif a < b:
    if b > c:
        print(b, " is the greatest")
    else:
        print(c, " is the greatest\n")

if a >= b and a >= c:
    maximum = a
else:
    if b >= c and b >= a:
        maximum = b
    else:
        maximum = c
print(maximum, " is the greatest")
