n, m = map(int, input().split())

for x in range(1, m+1):
    for y in range(1, n+1):
        if (x==1 or x==m) and (y==1 or y==n):
            print("+", end="")
        elif x==1 or x==m:
            print("-", end="")
        elif y==1 or y==n:
            print("|", end="")
        else:
            print(" ", end="")
    print()