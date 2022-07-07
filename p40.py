n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 > n2:
    if n1 > n3:
        print(n1, " is the greatest")
    else:
        print(n3, " is the greatest")
elif n2 > n1:
    if n2 > n3:
        print(n2, " is the greatest")
    else:
        print(n3, " is the greatest")