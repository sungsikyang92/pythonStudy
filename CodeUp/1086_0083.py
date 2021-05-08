w, h, d = input().split()
w = int(w)
h = int(h)
d = int(d)

print("%.2f MB" %(w*h*d/8/(1024**2)))