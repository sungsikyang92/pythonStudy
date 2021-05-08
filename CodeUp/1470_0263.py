import numpy as np

n = int(input())
nn = np.zeros((n, n), dtype=int)
num = 0

for x in range(n):
    if x % 2 != 0:
        for y in range(n-1, -1, -1):
            num += 1
            nn[x][y] = num
    else:
        for y in range(n):
            num += 1
            nn[x][y] = num

for i in range(0, n):
    for j in range(0, n):
        print(nn[j][i], end=' ')
    print()