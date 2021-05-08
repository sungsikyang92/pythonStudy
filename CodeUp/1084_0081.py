r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
c = 0
for x in range(r):
    for y in range(g):
        for z in range(b):
            c += 1
            print(x, y, z)
print(c)
