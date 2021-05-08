inp = int(input())
Box = 0
container = [5, 3]

for x in container:
    Box += inp // x
    inp %= x

print(Box)

#풀지 못함 ㅠ