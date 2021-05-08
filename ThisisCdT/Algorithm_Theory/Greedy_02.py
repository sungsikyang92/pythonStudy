#큰 수의 법칙
#5개의 숫자 8 번 더해야한다. 3번까지 연속해서 더 할 수 있다.

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

for x in range(len(nums)):
    print(nums[x], end=" ")

print((nums[-1]*k*(m//k))+(nums[-2]*(m % k)))

#2트

n, m, k = map(int, input().split())

num = list(map(int, input().split()))
num.sort()


first = num[-1]
second = num[-2]

x = m//k
y = m % k

result = (first*x*k)+(second*y)
print(result)