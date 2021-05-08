a, r, n =input().split()
a = int(a)
r = int(r)
n = int(n)
num = 1
for x in range(1, n):
    num = a * (r ** x)
print(num)