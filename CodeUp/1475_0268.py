n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(n)]for _ in range(m)]
count = 0

for x in range(m):
    if x % 2:
        for y in range(n-1,-1,-1):
            count += 1
            arr[x][y] = count
    else:
        for y in range(n):
            count += 1
            arr[x][y] = count

for x in range(n):
    for y in range(m-1,-1,-1):
        print(arr[y][x], end=" ")
    print()

# 1       2
# 0,0     0,1
# 4       3
# 1,0     1,1
# 5       6
# 2,0     2,1
#
#
# 5       4       1
# 2,0     1,0     0,0
# 6       3       2
# 2,1     1,1     0,1