n = int(input())

for x in range(1, n+1):
    for y in range(n):
        print(x+y*n, end=" ")
    print()