a, b = map(int, input().split())
result = 0
if a == b:
    if a % 2 == 0:
        print(a*2)
    else:
        print(0)
else:
    for x in range(a, b+1):
        if x % 2 != 0:
            result += x
        else:
            result -= x
print(result)