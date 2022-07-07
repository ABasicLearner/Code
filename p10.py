import math
n = int(input("Enter the decimal number: "))
s = 0
i = 0
while n >= 0:
    s = s + pow(10, i) * (n % 8)
    i = i + 1
    n = n // 8
    if n == 0:
        s = s + pow(10, i) * (n % 8)
        break
print(s)




"""num = int(input("Enter a number: "))
ans = 0
while num != 0:
    rem = num % 8
    ans = ans * 10 + rem
    num = num // 8
while ans != 0:
    octal = ans % 10
    ans = ans // 10
    print(octal, end='')"""

