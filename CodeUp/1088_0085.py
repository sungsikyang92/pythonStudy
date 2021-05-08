num = input()
num = int(num)

for x in range(1, num+1):
    if x % 3 == 0:
        continue
    print(x, end=" ")