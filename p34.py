n = int(input("Enter any number: "))
num = []
while n > 0:
    t = n % 10
    num.append(t)
    n = n // 10
num.sort()
val = int(num[-1])
li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print("The largest number is ", li[val])