yy, mm, dd = map(int, input().split(" "))
sum = str(yy+mm+dd)
if int(sum[-3]) % 2 == 0:
    print("대박")
else:
    print("그럭저럭")