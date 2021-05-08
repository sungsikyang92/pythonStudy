year = 2012
birth, num = input().split()
num = int(num)
if num == 1 or num == 2:
    birth = 1900 + int(str(birth[0:2]))
    age = year - birth + 1
    print(age)
elif num == 3 or num == 4:
    birth = 2000 + int(str(birth[0:2]))
    age = year - birth + 1
    print(age)