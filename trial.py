if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

        """
        gyiyudopf;,mnvsarrtyuiop;
        """

        x = 4  # x is of type int
        x = "Sally"  # x is now of type str
        print(x)

        x = 5
        y = "John"
        print(type(x))
        print(type(y))

        x, y, z = "Orange", "Banana", "Cherry"
        print(x)
        print(y)
        print(z)

#unpacking a collection
        fruits = ["apple", "banana", "cherry"]
        x, y, z = fruits
        print(x)
        print(y)
        print(z)

        x = "Python is "
        y = "awesome"
        z = x + y
        print(z)

x = 5
y = 10
print(x + y)

"""
x = 5
y = "John"
print(x + y)
"""

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

