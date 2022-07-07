# Write a Python Program to print equivalent binary number of given decimal number

num = int(input("Enter a number: "))
a = []
while num >= 0:
    rem = num % 2
    a.append(rem)
    num = num // 2
for i in a[-1::-1]:
    print(i, end='')


"""
import math
n = int(input("Enter the decimal number:  "))
s = 0
i = 0
while n >= 0:
    s += pow(10, i) * (n % 2)
    i += 1
    n //= 2
    if n == 0:
        s += pow(10, i) * (n % 2)
        break
print("Binary equivalent is ", s)
"""

