inp = int(input())

count = 0

if inp == 1 or inp == 3:
    count = -1
elif (inp % 5) % 2 == 0:
    count = (inp // 5) + (inp % 5) // 2
else:
    count = ((inp // 5) - 1 + (inp % 5 + 5) // 2)
print(count)