n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(m)]for _ in range(n)]
count = 0

for x in range(n+m-1):
    for y in range(m):
        for z in range(n):
            if y+z == x:
                count += 1
                arr[z][y] = count

for x in range(n):
    for y in range(m):
        print(arr[x][y], end=" ")
    print()