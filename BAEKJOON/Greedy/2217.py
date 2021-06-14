num = int(input())
rope = []
value = []

for i in range(num):
    rope.append(int(input()))
# 입력 확인
# print(rope)
rope.sort(reverse=True)
# print(rope)

for j in range(1, num+1):
    value.append(rope[j-1]* j )
print(max(value))