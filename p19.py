n = int(input("How many numbers you want to enter?: "))
arr = []
even = []
odd = []
print("Enter ", n, " elements one by one: ")
for i in range(n):
    p = int(input())
    arr.append(p)
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
print("list of even elements: ", even)
print("list of odd elements: ", odd)
