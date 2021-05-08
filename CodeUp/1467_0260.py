n, m = map(int, input().split())
for x in range(1, n+1):
    for y in range(m-1, -1, -1):
        print(y*n+x, end=" ")
    print()