n = 1260
count = 0

coin = [500, 100, 50, 10]

for change in coin:
    count += n // change
    n %= change

print(count)