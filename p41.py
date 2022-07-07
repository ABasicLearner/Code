n = int(input("Enter a number: "))
x = n
s = 0
while(x != 0):
    s = s + x % 10
    x = x // 10
print(s)