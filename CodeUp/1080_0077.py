num = input()
num = int(num)
s = 0
c = 0

for x in range(1, num+1):
    s += x
    c += 1
    if s >= num:
        break
print(c)