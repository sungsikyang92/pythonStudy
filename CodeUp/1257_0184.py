a, b = map(int,input().split())
if a != b :
    for x in range(a,b+1):
        if x % 2 != 0:
            print(x, end=" ")
else:
    for x in range(a,b+1):
        if x % 2 != 0:
            print(x)