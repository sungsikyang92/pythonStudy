play = list(map(int, input().split()))
# print(play.count(0))
c = play.count(1)
if c == 1:
    print("도")
elif c == 2:
    print("개")
elif c == 3:
    print("걸")
elif c == 4:
    print("윷")
else:
    print("모")