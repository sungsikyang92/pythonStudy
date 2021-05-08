n = int(input())
result = 1
count = 0
if result == n:
    print(n)
elif n % 10 == 0:
    n = str(n)
    print(len(n))
else:
    while result < n:
        result *= 10
        count += 1
    print(count)