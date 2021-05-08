num = input()
num = int(num)

for x in range(1, num+1):
    if x%3==0:
        print("X", end=" ")
    else:
        print(x, end=" ")