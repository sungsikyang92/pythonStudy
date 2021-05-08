a = int(input())
b = list(map(int, input().split()))
fifth = []
for x in b:
    if x % 5 == 0:
        fifth.append(x)
print(sum(fifth))