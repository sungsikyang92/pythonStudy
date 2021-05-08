n, m = map(int, input().split())

result = 0

for x in range(n):
    nums = list(map(int, input().split()))
    min_value = 10001
    for a in nums:
        min_value = min(min_value,a)
    result = max(result, min_value)

print(result)