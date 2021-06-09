N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

answer = []
num = 0

for x in range(N):
    num += K - 1
    if num >= len(arr):
        num = num % len(arr)

    answer.append(int(arr.pop(num)))

print("<",end="")
for j in range(N-1):
    print(answer[j],end=", ")
print(answer[-1],end="")
print(">",end="")
print()
print("".join(str(answer)).replace("[","<").replace("]",">"))
