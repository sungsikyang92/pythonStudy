n, k = map(int, input().split())

for x in range(n):
    for y in range(n):
        if y==0 or y==n-1 or x==0 or x==n-1:
            print("*", end="")
        elif (y + x + 1) % k == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()