time, score1, score2 = map(int, input().split())

if time % 10 == 0:
    score3 = (90 - time)//5
    if score1+score3 == score2:
        print("same")
    elif score1+score3 > score2:
        print("win")
    else:
        print("lose")
else:
    score3 = ((90 - time)//5) + 1
    if score1 + score3 == score2:
        print("same")
    elif score1 + score3 > score2:
        print("win")
    else:
        print("lose")