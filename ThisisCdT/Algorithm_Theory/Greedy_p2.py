num = input()
result = 0
result2 = 1

if int(num[0]) == 0:
    for x in range(len(num)):
        if x <= 1:
            result += int(num[x])
        elif x > 1:
            result *= int(num[x])
    print(result)
else:
    for x in range(len(num)):
        result2 *= int(num[x])
    print(result2)

