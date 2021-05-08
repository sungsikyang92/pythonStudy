car = 170
cave1, cave2, cave3 = map(int, input().split())
if cave1 > car :
    if cave2 > car :
        if cave3 > car :
            print("PASS")
        else:
            print("CRASH")
    else:
        print("CRASH")
else:
    print("CRASH")
