a, b = map(int, input().split())
if a % b == 0:
    print(str(b)+"*"+str(a//b)+"="+str(a))
elif b % a == 0:
    print(str(a)+"*"+str(b//a)+"="+str(b))
else:
    print("none")