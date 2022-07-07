n = int(input("Enter the decimal number: "))
s = ""
i = 0
while n >= 0:
    if n % 16 < 10:
        s = str(n % 16) + s
    if n % 16 == 10:
        s = 'A' + s
    if n % 16 == 11:
        s = 'B' + s
    if n % 16 == 12:
        s = 'C' + s
    if n % 16 == 13:
        s = 'D' + s
    if n % 16 == 14:
        s = 'E' + s
    if n % 16 == 15:
        s = 'F' + s
    n = n // 16
    if n == 0:
        break
print(s)