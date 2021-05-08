num = input()
num = int(num)
n = 0
for x in range(1, num+1):
    n += x
    if n >= num:
        break
print(n)