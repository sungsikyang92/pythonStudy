n = int(input())
record = {}

for x in range(n):
    name, score = input().split()
    record[name] = int(score)

sorted_rank = sorted(record.items(), key=lambda s: s[1], reverse=True)
print(sorted_rank[2][0])
