a = input()
b = input().split()

num = int(a)
arr = []

for x in range(num):
    arr.append(int(b[x]))
arr.reverse()
for x in range(num):
    print(arr[x], end=" ")