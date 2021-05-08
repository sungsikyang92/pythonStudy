n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(n)] for _ in range(m)]
count = 0

for z in range(n + m - 1):
    for x in range(m):
        for y in range(n):
            if x + y == z:
                count += 1
                arr[x][y] = count

for x in range(n):
    for y in range(m-1, -1, -1):
        print(arr[y][x], end=" ")
    print()

# 1       2
#
# 3       4
#
# 5       6