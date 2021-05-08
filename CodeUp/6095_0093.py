cb = [[0 for i in range(20)] for j in range(20)]


num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    cb[x-1][y-1] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(cb[i][j], end=' ')
    print()