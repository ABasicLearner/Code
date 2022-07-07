"""
def getMatrix():
    pMatrix = input("Enter all elements of matrix in row wise with spaces: ")
    pElements = pMatrix.split(" ")
    myMatrix = []
    for i in range(0,9):
        l = []
        l.append(int(pElements[i]))
        if((i+1)%3==0):
            myMatrix.append(l)
            l=[]
        return myMatrix
a= getMatrix()
b= getMatrix()
print(a)
print(b)


def getMatrix():
    pMatrix = input("Enter all elements of matrix in row wise with spaces: ")
    myMatrix = []
    for i in range(0,3):
        message = "Enter " + str(i) + " row elements"
        pElements = input(message)
        pMatrixelements = pElements.split(" ")
        l = []
        for p in pMatrixelements:
            l.append(int(p))
        myMatrix.append(l)
    return myMatrix
a= getMatrix()
b= getMatrix()
print(a)
print(b)
"""

#wap to find power of a number a^n
