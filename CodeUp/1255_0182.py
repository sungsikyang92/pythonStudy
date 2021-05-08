num = list(map(float, input().split()))
num.sort()
a = num[0]*100
b = num[1]*100
# print(a)
# print(b)
a = round(a)
b = round(b)
# print(a)
# print(b)
a = int(a)
b = int(b)
# print(a)
# print(b)

if a != b:
    for x in range(a, b+1):
        if x == 0.00:
            x = -0.00
        print("%.2f" % (x / 100), end=" ")
else:
    print(a / 100)