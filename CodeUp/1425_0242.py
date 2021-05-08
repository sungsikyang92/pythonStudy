sit = list(map(int, input().split()))
height = list(map(int, input().split()))
height.sort()
for x in range(int(sit[0]/sit[1])+1):
    for y in range(x*sit[1], x*sit[1]+sit[1]):
        if y >= len(height):
            break
        print(height[y], end=" ")
    print()