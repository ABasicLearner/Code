# topic: Exception handling

# e = 0
# logical error or dynamic error (here it is zero division error)
"""
There are two types of error - 1)static error (when there is mistake in the syntax)
                             - 2)dynamic error (when there is mistake in the logic og the program)
"""

"""
c = 4 % 0
print(c)   # giving error
"""

# Way of handling run-time error:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    c = a/b    # first interpreter try the division if error comes it goes to the except section
    print(c)
except Exception as e:     # "Exception as e" is optional
    # if coder doesn't want to show what kind of error it is to the user he/she can ignore using "exception as e"
    print("Entered invalid value\n", e)       # here e is the description of the error
print("Program ends here!")


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a/b
    print(c)
except ValueError as v:
    print("Error in input", v)
except ZeroDivisionError as z:
    print("Division by zero error")
except Exception as e:
    print(e)

# Go through the use of try... finally   eg. file handling
