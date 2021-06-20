n = int(input())
fear = list(map(int, input().split()))
fear.sort()

result = 0
count = 0
for x in fear:
    count += 1
    if count >= x:
        result += 1
        count = 0

print(result)