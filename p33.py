def getMatrix():
    print("Enter elements of 3*3 matrix row-wise with spaces:\n")
    aMatrix = []
    for i in range(3):
        message = "Enter row" + str(i+1) + " elements  "
        sElements = input(message)
        sMatrixElements = sElements.split(" ")
        l = []
        for j in sMatrixElements:
            l.append(int(j))
        aMatrix.append(l)
    return aMatrix


a = getMatrix()
Sum = 0
for i in range(3):
    l = []
    for j in range(3):
        if i == j:
           Sum = Sum + a[i][i]
print(Sum)