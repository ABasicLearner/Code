def get_matrix():
    n = input("Enter elements with spaces: ")
    a = n.split(" ")
    m = []
    l = []
    for i in range(0, 9):
        l.append(int(a[i]))
        if (i+1)%3 == 0:
            m.append(l)
            l = []
    return m
A = get_matrix()
print(A)
B = get_matrix()
print(B)
c = []
for i in range(3):
    l = []
    for j in range(3):
        l.append(A[i][j]+B[i][j])
    c.append(l)
print(c)


C = []
for i in range(3):
    l = []
    for j in range(3):
        sum = 0
        for k in range(3):
            sum = sum + (A[i][k] * B[k][j])
        l.append(sum)
    C.append(l)
print(C)
