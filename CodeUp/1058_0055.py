a, b = input().split(" ")
a = bool(int(a))
b = bool(int(b))
print(int((not a) and (not b)))