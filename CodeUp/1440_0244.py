n = int(input())
num = list(map(int, input().split()))
for y in range(n):
    print("%d:" %(y+1), end=" ")
    for x in range(n):
        if y == x:
            continue
        if num[y] > num[x]:
            print(">", end=" ")
        elif num[y] < num[x]:
            print("<", end=" ")
        else:
            print("=", end=" ")
    print()