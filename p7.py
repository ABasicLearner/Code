# Write a Python Program to find the position of given number in array

"""list1 = [92, 4, 11, 3, 0, -8]
print(list1)
n = int(input("Enter a number to find its position in the list: "))
print(n, "is at index", list1.index(n))
"""

'''
value = input("Enter any string with spaces")
listName = value.split(" ")
print(listName)
n = input("Enter a number to find its position in the list: ")
print(n, "is at index", listName.index(n))
'''


n = int(input("How many numbers you want to enter? \n"))
a = []
flag = 0
print("Enter ", n, "elements one by one:\n")
for i in range(n):
    p = int(input())
    a.append(p)
print(a)
num = int(input("Enter a number to get its position in the array: "))
for i in range(n):
    if a[i] == num:
        flag = 1
        print(num, " is at ", "position ", i+1)
        break
if flag == 0:
    print(num, " not found!")


