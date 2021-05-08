n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(n)] for _ in range(m)]
count = 0

for z in range(n + m - 1):
    for x in range(m-1,-1,-1):
        for y in range(n-1,-1,-1):
            if x + y == z:
                count += 1
                arr[x][y] = count

for x in range(n-1,-1,-1):
    for y in range(m):
        print(arr[y][x], end=" ")
    print()

# 1 3 6 9
# 2 5 8 11
# 4 7 10 12
#
# 1 2 4 7
# 3 5 8 10
# 6 9 11 12
#
# 6 9 11 12
# 3 5 8 10
# 1 2 4 7
#
# 12 11 9 6
# 10 8 5 3
# 7 4 2 1