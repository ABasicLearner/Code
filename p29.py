def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
g = gcd(n1, n2)
print("gcd of ", n1, "& ", n2, " is: ", g)



"""
 if n1 == n2:
            return n1
        elif n1 > n2:
            return 
"""