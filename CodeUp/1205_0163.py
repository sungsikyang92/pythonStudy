a, b = map(int, input().split())
c = a + b
d = a - b
e = b - a
f = a * b
g = a / b
h = b / a
i = a**b
j = b**a
list=[c,d,e,f,g,h,i,j]
print("%.6f" %max(list))
