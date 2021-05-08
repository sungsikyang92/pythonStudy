n = int(input())

for x in range(1, n+1):
    for y in range(x):
        print("*", end="")
    print()
for x in range(n-1, 0, -1):
    for y in range(x):
        print("*", end="")
    print()