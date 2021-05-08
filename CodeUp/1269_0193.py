a, b, c, n = map(int, input().split())

for x in range(n):
    if x == 0:
        a
    else:
        a = (a * b) + c
print(a)