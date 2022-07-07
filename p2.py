# Write a Python Program to sort an array in ascending order

"""arr = [2, 4, 56, -98, 0, 13]
#a = sorted(arr)
arr.sort()
print(arr)
"""


# w/o using sort() method
n = int(input("How many elements in array: "))
arr = []
print("Enter ", n, "elements one by one:\n")
for i in range(n):
    m = int(input())
    arr.append(m)
print(arr)
a = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            a = arr[i]
            arr[i] = arr[j]
            arr[j] = a
print(arr)

"""
s = input("Enter list elements with spaces: ")
list1 = s.split(" ")
n = len(list1)
k = 0
list2 = []
alist = []
for i in range(n):
    list2[i] = int(list1[i])
for i in range(n):
    for j in range(i+1, n):
        if list2[i] > list2[j]:
            alist.append(list1[i])
        else:
            alist.append(list1[j])
print(alist)
"""

