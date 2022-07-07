n = int(input("Enter a number to get its factorial: "))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(n, "! = ", fact(n))
