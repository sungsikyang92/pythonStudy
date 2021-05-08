h, w = input().split()

# 격자판 만들기(좌표를 그대로 사용하기 위해서 +1 해준다)
cb = [[0 for y in range(int(w)+1)]for x in range(int(h)+1)]

# 격자판 확인(좌표를 그대로 사용하기 위해서 1부터 시작하고 +1씩 해준다)
# for x in range(1, int(h)+1):
#     for y in range(1, int(w)+1):
#         print(cb[x][y], end=" ")
#     print()

# 막대의 개수
n = int(input())

# 막대의 개수만큼 칸을 칠해야 한다.
for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    if d == 0:
        for x in range(x, x+1):
            for y in range(y, y+l):
                cb[x][y] = 1
    else:
        for x in range(x, x+l):
            for y in range(y, y+1):
                cb[x][y] = 1

# 설탕과자 뽑기 출력
for i in range(1, int(h)+1):
    for j in range(1, int(w)+1):
        print(cb[i][j], end=" ")
    print()