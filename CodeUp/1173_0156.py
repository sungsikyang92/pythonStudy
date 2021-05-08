hrs, mins = map(int, input().split())

if hrs == 0 :
    if mins < 30:
        hrs = 23
        mins += 30
        print(hrs, mins)
    else:
        hrs = 0
        mins -= 30
        print(hrs, mins)
else:
    if mins < 30:
        hrs -= 1
        mins += 30
        print(hrs, mins)
    else:
        mins -= 30
        print(hrs, mins)