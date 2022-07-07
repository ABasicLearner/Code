n= int(input("Enter a number: "))
f = 0
for i in range(2,n):
    if n % i == 0:
        print(n, " is not prime")
        f = 1
        break
if f == 0:
    print(n, " is prime")
