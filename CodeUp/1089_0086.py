a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

for x in range(n-1):
    a += d
print(a)