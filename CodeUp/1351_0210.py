a, b = map(int, input().split())

for x in range(a, b+1):
    for y in range(1, 10):
        print("%d*%d=%d" %(x, y, (x*y)))