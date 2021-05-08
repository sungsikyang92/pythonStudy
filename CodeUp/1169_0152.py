sy = 2012
age = int(input())
birth = sy - age + 1
if birth < 2000:
    print(birth-1900, 1)
else:
    print(birth-2000, 3)