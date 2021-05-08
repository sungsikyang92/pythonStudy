n = int(input())

for x in range(n):
    if x % 2 == 0:
        for y in range(1, n+1):
            print((n*x)+y, end=" ")
    else:
        for y in range(n, 0, -1):
            print((x*n)+y, end=" ")
    print()