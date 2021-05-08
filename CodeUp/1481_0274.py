n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(n)]for _ in range(m)]
count = 0

for z in range(n + m - 1):
    for x in range(m-1,-1,-1):
        for y in range(n-1,-1,-1):
            if x+y == z:
                count += 1
                arr[x][y] = count

for x in range(n-1,-1,-1):
    for y in range(m-1,-1,-1):
        print(arr[y][x], end=" ")
    print()

# 6       5       3
# 00      01      02
# 4       2       1
# 10      11      12
