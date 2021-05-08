n, m = map(int, input().split())

for x in range(n-1, -1, -1):
    for y in range(1, m+1):
        print(x*m+y, end= " ")
    print()