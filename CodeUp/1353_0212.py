n = int(input())
# row = 0
# for x in range(n-n+1):
#     for y in range(n):
#         row += 1
#         print("*"*row)
#     print()

for i in range(1, n+1):
    for j in range(0, i):
        print("*", end="")
    print()