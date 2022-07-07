def getMatrix():
    print("Enter elements of 3*3 matrix row-wise with spaces:\n")
    aMatrix = []
    for i in range(3):
        sElements = input("Enter row" + str(i+1) + " elements  ")
        sMatrixElements = sElements.split(" ")
        l = []
        for j in sMatrixElements:
            l.append(int(j))
        aMatrix.append(l)
    return aMatrix


a = getMatrix()
b = getMatrix()
c = []
for i in range(3):
    l = []
    for j in range(3):
        Sum = 0
        for k in range(3):
            Sum = Sum + a[i][k] * a[k][j]
        l.append(Sum)
    c.append(l)

print("Multiplication od matrix A with B is: ")
for i in c:
     print(i)