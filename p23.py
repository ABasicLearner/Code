def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

n = int(input("Enter a number: "))
s = 0
for i in range(1, n+1):
    s = s + (i/fact(i))
print(s)