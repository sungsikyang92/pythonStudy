n = int(input())
for x in range(n):
    if (x == 0) or (x == n-1):  #첫 번쨰 줄, 마지막 줄
        for y in range(n):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for y in range(0, n-2): #마지막 줄 이전까지
            print(" ", end="")
        print("*", end="")
        print()