# Transpose of a matrix

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
A = getMatrix()
print("Entered matrix:")
for i in A:
    print(i)

# transpose
B = []
for i in range(3):
    l = []
    for j in range(3):
        l.append(A[j][i])
    B.append(l)
print("\nTranspose matrix: ")
for i in B:
    print(i)
