c = input("Enter a character: ")

ch = ord(c)
if ch >= ord('0') and ch <= ord('9'):
    print(c, " is a digit!")
elif (ch >= ord('A') and ch <= ord('Z')) or (ch >= ord('a') and ch <= ord('z')):
    print(c, "is an alphabet!")
else:
    print(c, " is a special character!")
