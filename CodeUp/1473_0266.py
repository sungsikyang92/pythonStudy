n, m = map(int, input().split())
arr = [[0 for _ in range(m)]for _ in range(n)]
count = 0

for x in range(n):
    for y in range(m):
        count += 1
        arr[x][y] = count

for x in range(n-1,-1,-1):
    if x % 2:
        for y in range(m-1,-1,-1):
            print(arr[x][y], end=" ")
    else:
        for y in range(m):
            print(arr[x][y], end=" ")
    print()

#
# 1       2      3
# 0,0     0,1     0,2
# 4       5      6
# 1,0     1,1     1,2
#
# 6       5       4
# 1,2     1,1     1,0
# 1       2       3
# 0,0     0,1     0,2