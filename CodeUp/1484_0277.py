a, b = map(int, input().split())
arr = [[0 for _ in range(b)]for _ in range(a)]
count = 0
d = 0
n = a
m = b
while count < n*m:
    for x in range(d, m-d):
        count += 1
        arr[d][x] = count

    for x in range(d+1, n-d):
        count += 1
        arr[x][m-d-1] = count

    for x in range(m-d-1, d, -1):
        count += 1
        arr[n-d-1][x-1] = count

    for x in range(n-d-2, d, -1):
        count += 1
        arr[x][d] = count
    d += 1
    n -= 1
    m -= 1

for x in range(a):
    for y in range(b):
        print(arr[x][y], end=" ")
    print()