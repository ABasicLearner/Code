"""f = open("E:\\foo.txt", "w")
f.write("Now this file has some content!\n Python is an interesting language")
f.close()

f = open("foo.txt", "r")
print(f.read())
"""

fo = open("E:\\f1.txt", "w")
fo.write("Now this file has some content!\n Python is an interesting langauge")

"""fo = open("E:\\f1.txt", "r+")
str = fo.read()
print("Read string: ", str)
fo.close()

fo = open("E:\\f1.txt", "r+")
fo.write("what")"""

fo = open("E:\\f1.txt", "a")
fo.write("Algebra")
fo.seek(0)
s=fo.read()
print("read",s)
fo.close()
