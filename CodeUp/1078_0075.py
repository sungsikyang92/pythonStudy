num = input()
num = int(num)
sum=0
for n in range(1, num+1):
    if n % 2 == 0:
        sum+=n
print(sum)