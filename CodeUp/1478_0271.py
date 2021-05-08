n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(m)]for _ in range(n)]
count = 0

for z in range(n+m-1):
    for x in range(n):
        for y in range(m-1, -1, -1):
            if x+y == z:
                count += 1
                arr[x][y] = count

for x in range(n):
    for y in range(m-1, -1, -1):
        print(arr[x][y], end=" ")
    print()