for i in range(1, 500):
    s = 0
    t = i
    l = len(str(t))
    while t != 0:
        r = t % 10
        s = s + (r ** l)
        t = t // 10
    if s == i:
        print(i)



# checking if entered number is armstrong
"""n = int(input("Enter a number: "))
s = 0
while n > 0:
    r = n % 10
    s = s + pow(n, 3)
    n = n // 10
if s == n:
     print("Armstrong")
else:
    print("Not armstrong")
"""