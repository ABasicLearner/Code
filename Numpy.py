import numpy as np
import matplotlib.pyplot as plt
# 1
a = np.arange(12, 86)
print(a)

print()

# 2
arr = np.array([1, 7, 2, 4, 0, 22, 8])
print("Original array", str(arr))
rev = arr[::-1]
print("Reverse array is: ", rev)

print()

# 3
n = int(input("Enter n: "))
x = np.ones((n, n))
x[1:-1, 1:-1] = 0
print(x)

print()

# 4
A = [[1, 2, 4], [2, 7, 9]]
B = [[3, 5], [3, 7], [2, 3]]
print(np.dot(A, B))

print()

# 5
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday's date: ", yesterday)
today = np.datetime64('today', 'D')
print("Today's date: ", today)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow's date: ", tomorrow)

print()

# 6
print("Number of days in February 2016:")
print(np.datetime64('2016-03-01') - np.datetime64('2016-02-01'))
print("Number of days in March 2016:")
print(np.datetime64('2016-04-01') - np.datetime64('2016-03-01'))
print("Number of days in February 2017:")
print(np.datetime64('2017-03-01') - np.datetime64('2017-02-01'))

print()

# 7
r1 = int(input("Enter number of rows: "))
c1 = int(input("Enter number of columns: "))
a = np.zeros((r1, c1), dtype=int)
for i in range(r1):
    for j in range(c1):
        x = int(input("Enter element: "))
        a[i][j] = x
print(a)
r2 = int(input("Enter number of rows: "))
c2 = int(input("Enter number of columns: "))
b = np.zeros((r2, c2), dtype=int)
for i in range(r2):
    for j in range(c2):
        x = int(input("Enter element: "))
        b[i][j] = x
print(b)
print()
if c1 == r2:
    c = np.dot(a, b)
    print(c)
else:
    print("Matrix multiplication is not possible!")

print()

# 8
x = [1, 2]
y = [3, 4]
res = np.cross(x, y)
print(res)

print()

# 9
m = np.array([[1, 2, 0], [1, 3, 4]])
SumOfDiag = np.trace(m)
print("Trace of matrix\n", m, " is ", SumOfDiag)

print()

# 10
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int)
for i in range(9):
    if a[i] % 2 != 0:
        a[i] = -1
print(a)

print()

# 11
arr = np.array([1, 2, 4, 7, 6, 9, 0, 1, 0])
print("Before reshaping: ", arr)
arr1 = arr.reshape(3, 3)
print("After reshaping 1D array into 2D: ")
print(arr1)

print()

# 12
x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

print()

# 13
x = np.arange(0, 4*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.show()

print()

# 14
x = np.arange(-50, 50)
y = x * x
plt.plot(x, y)
plt.show()

print()

# 15
x = np.arange(-50, 50)
y = x * x * x
plt.plot(x, y)
plt.show()
