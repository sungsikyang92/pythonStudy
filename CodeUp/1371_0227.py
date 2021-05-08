n = int(input())

for x in range(n):
    for y in range(n-x-1, 0, -1):
        print(" ", end="")
    print("*", end="")
    for y in range(0, x*2):
        print(" ", end="")
    print("*")
for x in range(n):
    for y in range(n):
        print(" ", end="")
    print("*", end="")
    for y in range((n-x-1)*2, 0, -1):
        print(" ", end="")
    print("*")