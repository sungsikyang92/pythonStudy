n = int(input())
arr = [[0 for _ in range(n)]for _ in range(n)]
count = 0

for x in range(n):
    if x % 2:
        for y in range(n-1,-1,-1):
            count += 1
            arr[x][y] = count
    else:
        for y in range(n):
            count += 1
            arr[x][y] = count

for x in range(n-1,-1,-1):
    for y in range(n):
        print(arr[y][x], end=" ")
    print()