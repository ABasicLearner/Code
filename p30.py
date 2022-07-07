a = input("Enter any string: ")
countword = 1
countchar = 0
for i in a:
    if i == ' ':
        countword += 1
    countchar += 1
print("Character count is ", countchar)
print("Word count is ", countword)
