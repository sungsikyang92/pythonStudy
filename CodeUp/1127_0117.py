sum = 0
for x in range(3):
    a, b = map(float, input().split())
    sum = sum +(a*b)
print("%.1f" % sum)