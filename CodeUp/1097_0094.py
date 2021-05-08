# 바둑판 준비
cb = [[0 for i in range(20)] for j in range(20)]

# 바둑판 input
for x in range(19):
    black = input().split()
    for y in range(19):
        cb[x+1][y+1] = int(black[y])

# 뒤집기 횟수
num = int(input())

# 뒤집기
for x in range(num):
    a, b = input().split()
    for y in range(1, 20):
        if cb[y][int(b)] == 0:
            cb[y][int(b)] = 1
        else:
            cb[y][int(b)] = 0

        if cb[int(a)][y] == 0:
            cb[int(a)][y] = 1
        else:
            cb[int(a)][y] = 0

#출력
for x in range(1, 20):
    for y in range(1, 20):
        print(cb[x][y], end=' ')
    print()