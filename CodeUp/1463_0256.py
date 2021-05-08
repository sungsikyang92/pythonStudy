n = int(input())

for x in range(n):
    for y in range(1, n+1):
        print(n*y-x, end=" ")
    print()