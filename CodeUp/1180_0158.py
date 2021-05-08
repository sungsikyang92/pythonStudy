size = input()
# print("%02d" % int(str(size[::-1])))
size = int(str(size[::-1]))
nsize = size * 2
# print(size)
if (nsize%100) <= 50:
    if nsize > 100:
        print(nsize-100)
        print("GOOD")
    else:
        print(nsize)
        print("GOOD")
else:
    if nsize > 100:
        print(nsize-100)
        print("OH MY GOD")
    else:
        print(nsize)
        print("OH MY GOD")