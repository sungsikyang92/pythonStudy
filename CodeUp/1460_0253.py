n = int(input())
for x in range(n):
    for y in range((x*n)+1, (x*n)+n+1):
        print(y, end=" ")
    print()