# Write a Python Program to print square of all numbers 1 to 20 and print sum squares

squareSum = 0
for i in range(1, 21):
    square = pow(i, 2)
    squareSum = squareSum + square
    print(i, '*', i, '=', square)
print('Sum of squares from 1 to 20 is', squareSum)
