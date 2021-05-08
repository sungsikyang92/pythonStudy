k = int(input())

for x in range(1, 7):
    for y in range(6, 0, -1):
        if x+y == k:
            print(x, y)