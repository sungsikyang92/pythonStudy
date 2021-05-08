n, m = map(int,input().split())
arr = [[0 for _ in range(m)]for _ in range(n)]
count = 0

for x in range(m):
    if x % 2:
        for y in range(n):
            count += 1
            arr[y][x] = count
    else:
        for y in range(n-1,-1,-1):
            count += 1
            arr[y][x] = count

for x in range(n):
    for y in range(m-1,-1,-1):
        print(arr[x][y], end=" ")
    print()


# 2       1
# 0,0     0,1
# 3       4
# 1,0     1,1
# 6       5
# 2,0     2,1
#
# 6       3       2
# 2,0     1,0     0,0
# 5       4       1
# 2,1     1,1     0,1