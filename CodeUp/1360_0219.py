n =int(input())

for x in range(n, 0, -1):
    for y in range(x, 0, -1):
        print(x, end=" ")
    print()