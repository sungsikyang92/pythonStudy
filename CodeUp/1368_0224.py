h, k, d = input().split()
h = int(h)
k = int(k)

if d == "L":
    for x in range(h):
        for y in range(x):
            print(" ", end="")
        for y in range(k):
            print("*", end="")
        print()
else:
    for x in range(h-1, -1, -1):
        for y in range(x):
            print(" ", end="")
        for y in range(k):
            print("*", end="")
        print()