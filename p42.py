n = int(input("Enter a number: "))
while n != 0:
    rem = n % 10
    n = n // 10
    print(rem, end='')

"""
n = int(input("Enter a number"))
x = n
s = 0
while x != 0:
    s = s * 10 + x % 10
    x = x // 10
print("reverse of ", n, " is ", s)
"""