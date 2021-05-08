a = int(input())
b = list(map(int, input().split()))
# print(sum(b))
s = 0
for x in b:
    s += x
print(s)