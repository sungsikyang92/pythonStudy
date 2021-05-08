yy, mm, dd = map(int, input().split(" "))
sum = str(yy - mm + dd)
if sum[-1] == "0":
    print("대박")
else:
    print("그럭저럭")