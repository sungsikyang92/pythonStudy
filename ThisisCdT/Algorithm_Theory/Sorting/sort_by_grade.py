n = int(input())
score = []
for _ in range(n):
    inp = input().split()
    score.append((inp[0], int(inp[1])))

print(score)
result = sorted(score, key=lambda student: student[1])

print(result)