N, M, K = map(int, input().strip().split())
# print(N, M, K)
num = list(map(int, input().strip().split()))

num.sort(reverse=True)
# print(num)
sum = 0

first = num[0]
second = num[1]

while True:
    for i in range(K):
        if M == 0:
            break
        sum += first
        M -= 1
    if M == 0:
        break
    sum += second
    M -= 1

print(sum)