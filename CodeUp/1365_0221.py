n = int(input())

#첫째줄
for x in range(n):
    print("*", end="")
print()

#중간줄들
for x in range(1, n-1):
    for y in range(n):
        if y==0 or y==x or y==n-1 or y==n-x-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#마지막줄
for x in range(n):
    print("*", end="")