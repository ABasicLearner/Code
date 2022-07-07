n = int(input("Enter a number: "))
p = 1
for i in range(2,n):
    if n % i == 0:
        print(n, " is not prime")
        p = 0
        break
if p == 1:
    print(n, " is prime")