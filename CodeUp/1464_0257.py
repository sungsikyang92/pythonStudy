n, m = map(int, input().split())

for x in range(n, 0, -1):
    for y in range(m):
        print(m*x-y, end=" ")
    print()