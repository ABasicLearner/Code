# addition of two matrices
"""def getMatrix():
    smatrix = input("Enter elements of matrix row wise using spaces:")
    selements = smatrix.split(" ")
    amatrix = []
    l = []
    for i in range(0,9):
        l.append(int(selements[i]))
        if (i+1) % 3 == 0:
            amatrix.append(l)
            l = []
    return amatrix

a = getMatrix()
"""



def getMatrix():
    print("Enter row wise: ")
    amatrix = []
    l = []
    for i in range(3):
        selements = input("Enter elements of row " + str(i+1) + ": ")
        smatrixelements = selements.split(" ")
        for j in smatrixelements:
            l = []
            l.append(int(j))
        amatrix.append(l)
    return amatrix


a = getMatrix()
b = getMatrix()
c = []
for i in range(3):
    p = []
    for j in range(3):
        p.append(a[i][j] + b[i][j])
    c.append(p)
print(c)
