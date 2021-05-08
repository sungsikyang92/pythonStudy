n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
biggest = nums[-1]
second = nums[-2]

result = 0
while True:
    for x in range(k):
        if m == 0:
            break
        result += biggest
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)