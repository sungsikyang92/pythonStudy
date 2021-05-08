al = list(map(ord, input().split()))
al.sort()
# print(al)
for x in range(al[0], al[1]+1):
    print(chr(x), end=" ")