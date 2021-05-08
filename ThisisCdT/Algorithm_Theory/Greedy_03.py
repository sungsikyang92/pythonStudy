n, m = map(int, input().split())

result = 0

for x in range(n):
    arr = list(map(int, input().split()))
    print(min(arr))
    min_val = min(arr)
    result = max(result, min_val)
print(result)


#2트

n, m = map(int, input().split())
min_value = []
for row in range(n):
    arr = list(map(int, input().split()))
    min_value.append(min(arr))

print(max(min_value))

