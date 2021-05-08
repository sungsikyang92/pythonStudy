a = int(input())
num = list(map(int, input().split()))
max = num[0]

for x in num:
    if x > max:
        max = x
print(max)