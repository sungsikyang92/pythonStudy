num = list(map(int, input().split()))
num.sort()
for x in range(num[0], num[1]+1):
    print(x, end=" ")