"""
year = input("enter year")
y = int(year)
if y % 4 != 0:
    print("not leap")
else:
    if y % 100 == 0:
        if y % 400 == 0:
            print('leap')
        else:
            print('not leap')
    else:
        print('leap')
"""

year = int(input('Enter year to check if it is leap or not:'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("leap year")
else:
    print("not a leap year")
