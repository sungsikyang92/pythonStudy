#실패

n, k = map(int, input().split())
count = 0
for x in range(n, 0, -1):
    if x % k != 0:
        count += 1
        n -= 1
    elif x % k == 0:
        count += 1
        n = n // k
    if n == 1:
        break

print(count)

#2트

n, k = map(int, input().split())
count = 0

while True:
    if n % k == 0:
        count += 1
        n = n // k
    elif n % k != 0:
        count += 1
        n -= 1
    if n == 1:
        break
print(count)

