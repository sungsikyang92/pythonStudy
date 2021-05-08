n, k = map(int, input().split())
result = 1
for x in range(0, k):
    result *= n
print(result)