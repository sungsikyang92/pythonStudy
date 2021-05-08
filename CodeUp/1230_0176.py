car = 170
a, b, c = map(int, input().split())
while True:
    if a <= car:
        print("CRASH %d" % a)
        break
    else:
        if b <= car:
            print("CRASH %d" % b)
            break
        else:
            if c <= car:
                print("CRASH %d" % c)
                break
            else:
                print("PASS")

if a <= car:
    print("CRASH %d" % a)
elif b <= car:
    print("CRASH %d" % b)
elif c <= car:
    print("CRASH %d" % c)
else:
    print("PASS")