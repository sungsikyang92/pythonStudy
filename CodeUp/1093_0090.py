a = input()
b = input().split()

number = int(a)
arr = []

for x in range(24):
    arr.append(0)

for x in range(number):
    arr[int(b[x])] += 1

for x in range(1, 24):
    print(arr[x], end=" ")
