# Write a Python Program to check if given number is present in an array or not

n = int(input("How many numbers do you want to enter? "))
arr = []
print("Enter ", n, " elements one by one:\n")
for i in range(n):
    a = int(input())
    arr.append(a)
print(arr)
num = int(input("Enter a number to check its presence in the array: "))
present = 0
for r in arr:                                # for i in range(n):
    if num == r:                                    # if arr[i] == num:
        present = 1
if present == 1:
    print("Present")
else:
    print("Absent")
