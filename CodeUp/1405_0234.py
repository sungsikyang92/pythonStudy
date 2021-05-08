n = int(input())
num = list(map(int, input().split()))

for x in range(n, 0, -1):
    for y in range(n):
        print(num[y-x], end=" ")
    print()