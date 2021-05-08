h, r = map(int, input().split())
def zig(h):
    for x in range(h):
        for y in range(h):
            if y==x:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for x in range(h-1,0,-1):
        for y in range(h-1):
            if y==(x-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

for x in range(r):
    zig(h)