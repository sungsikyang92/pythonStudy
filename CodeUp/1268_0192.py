a = int(input())
b = list(map(int, input().split()))
d = []
for x in b:
    if x % 2 == 0:
      d.append(x)
print(len(d))