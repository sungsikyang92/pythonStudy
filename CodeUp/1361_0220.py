n = int(input())

for x in range(n):
    for y in range(x):
        print(" ", end="")
    for y in range(2):
        print("*", end="")
    print()