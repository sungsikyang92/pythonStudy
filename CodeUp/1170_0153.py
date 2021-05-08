a, b, c = input().split()
if 0 < int(c) < 10:
    print(a+b+"0"+c)
else:
    print(a+b+c)