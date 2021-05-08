n, m = map(int, input().split())

for x in range(n, 0, -1):
    for y in range(m-1, -1, -1):
        print(n*y+x, end=" ")
    print()