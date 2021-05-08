n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
first = nums[-1]
second = nums[-2]

count_first = int(m/(k+1)) * k
count_first += m % (k+1)

result = 0
result += (count_first) * first
result += (m - count_first) * second

print(result)