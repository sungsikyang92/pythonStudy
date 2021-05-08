# 개미집 만들기 10 x 10
house = [[0 for y in range(11)]for x in range(11)]

# 외벽 및 장애물 집어넣기(+1을 한 이유는 입려되는 숫자가 0이아닌 1부터 시작하기 때문이다)
for i in range(10):
    wall = input().split()
    for j in range(10):
        house[i+1][j+1] = int(wall[j])

x = 2
y = 2

while True:
    if house[x][y] == 0:
        house[x][y] = 9
    elif house[x][y] == 2:
        house[x][y] = 9
        break

    if house[x][y+1] == 1 and house[x+1][y] == 1:
        break

    if house[x][y+1] != 1:
        y += 1
    elif house[x+1][y] != 1:
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(house[i][j], end=" ")
    print()