a, b =input().split(" ")
a = bool(int(a))
b = bool(int(b))
print(int((a==True and b==False)or(a==False and b==True)))