N, K = map(int, input().strip().split())
count = 0

while True:
    if N % K != 0:
        N -= 1
        count += 1
        if N == 1:
            break
    else:
        N /= K
        count += 1
        if N == 1:
            break

print(count)