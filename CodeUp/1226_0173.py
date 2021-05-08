lottery = list(map(int, input().split()))
mynumber = list(map(int, input().split()))
isBonus = False
bonusnum = lottery[6]
del lottery[6]
matchNumber = 0
lottery.sort()
mynumber.sort()

for lot in lottery:
    for num in mynumber:
        if lot == num:
            matchNumber += 1

if matchNumber == 6:
    print(1)
elif matchNumber == 5:
    for num in mynumber:
        if num == bonusnum:
            isBonus = True
            break
        else:
            isBonus = False
    if isBonus == True:
        print(2)
    else:
        print(3)
elif matchNumber == 4:
    print(4)
elif matchNumber == 3:
    print(5)
else:
    print(0)