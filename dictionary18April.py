"""
dict1 = {1:"Hello", 2: "Hi", 3: "Namaste"}
print(dict1)

# replacing value of key 2
dict1[2] = "Bye"
print(dict1)

# adding new element
dict1[4] = "Hi"
print(dict1)

dict2 = {5: "Priti"}
dict1.update(dict2)       # update function to merge two dictionaries
print(dict1)

for k in dict1.keys():
    print("key:", k, "value:", dict1[k])     # displays key and their value one by one



s1 = [1, "a", 7, "b", 3, "c", 4, "d"]
dic = {}
dic2 = {}
i = 0
for e in s1:     # to create a dictionary from a list
    dic[i] = e
    i += 1
for i in range(0, len(s1)):    # creating a dictionary from a list
    dic2[i] = s1[i]
print(dic)
print(dic2)


"""

a = 6
b = 3
c = a/b    # gives quotient in float
d = a//b   # gives quotient in integer
print(c)
print(d)



