n = int(input())

#첫째줄
for x in range(n):
    print("*", end="")
print()

#중간영역1
for x in range(1, int(n/2)):
    for y in range(n):
        if y==0 or y==x or y==n-1 or y==n-x-1 or y==int(n/2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#중간줄
for x in range(n):
    print("*", end="")
print()

#중간영역2
for x in range(int(n/2)-1,0,-1):
    for y in range(n):
        if y==0 or y==x or y==n-1 or y==n-x-1 or y==int(n/2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
#마지막줄
for x in range(n):
    print("*", end="")
print()