import numpy as np
n, m = map(int, input().split())
arr = np.zeros((n, m), dtype=int)
count = 0

for x in range(n):
    for y in range(m):
        count += 1
        arr[x][y] = count

for x in range(n-1,-1,-1):
    if x % 2:
        for y in range(m):
            print(arr[x][y], end=" ")
    else:
        for y in range(m-1,-1,-1):
            print(arr[x][y], end=" ")
    print()

#numpy 미사용
n, m = map(int, input().split())
arr = [[0 for _ in range(m)]for _ in range(n)]
count = 0

for x in range(n):
    for y in range(m):
        count += 1
        arr[x][y] = count

for x in range(n-1,-1,-1):
    if x % 2:
        for y in range(m):
            print(arr[x][y], end=" ")
    else:
        for y in range(m-1,-1,-1):
            print(arr[x][y], end=" ")
    print()