a, b = map(int, input().split())
sum = 0
if a != b:
    for x in range(a, b+1):
        if x % 3 ==0:
            sum += x
    print(sum)
else:
    for x in range(a, b + 1):
        if x % 3 == 0:
            print(a)
        else:
            print(0)