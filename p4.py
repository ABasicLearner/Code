# Write a Python Program to find sum of digits in a given number

num = int(input("Enter a number: "))
Sum = 0
while num != 0:
    rem = num % 10
    Sum = Sum + rem
    num = num // 10
print(Sum)
