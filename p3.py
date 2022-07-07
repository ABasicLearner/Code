# Write a Python Program to sort an array in descending order

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
        if arr[i] < arr[j]:
            a = arr[i]
            arr[i] = arr[j]
            arr[j] = a
print(arr)
