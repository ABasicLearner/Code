def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


n = int(input("Enter a number: "))
s = 0
for j in range(1, n+1):
    s = s + fact(j)
print(s)



"""
f = 1
s = 0
for i in range(1, n+1):
    f = f * i
    s = s + f
print(s)
"""