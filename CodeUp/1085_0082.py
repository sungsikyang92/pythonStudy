h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

print("%0.1f" %((h*b*c*s)/8/(1024**2)), end=" MB")