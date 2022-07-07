def get_matrix():
    print("Enter elements of 3*3 matrix row-wise with spaces:")
    a_matrix = []

    for i in range(3):
        s_elements = input("Enter elements of row" + str(i+1) + ": ")
        s_matrix_elements = s_elements.split(" ")
        l = []
        for j in s_matrix_elements:
            l.append(int(j))
        a_matrix.append(l)
    return a_matrix


A = get_matrix()
for i in A:
    print(i)

# largest element
max = A[0][0]
for i in range(3):
    for j in range(3):
        if max < A[i][j]:
            max = A[i][j]
print("The largest element in the matrix is: ", max)
