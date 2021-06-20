N, M = map(int, input().strip().split())
# print(N, M)
result = 0
for i in range(N):
    num = list(map(int, input().strip().split()))
    min_val = min(num)
    result = max(result, min_val)


print(result)

