n = int(input())

for x in range(n + n - 1, n-1, -1):
    for y in range(x - n):
        print(" ", end="")
    for y in range(n):
        print("*", end="")
    print()
