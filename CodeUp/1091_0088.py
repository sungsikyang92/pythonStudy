a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for x in range(1, n):
    a = a * m +d
print(a)