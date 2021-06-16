inp = int(input())

stack = []
count = 0
result = []

for _ in range(inp):
    num = int(input())

    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")

    else:
        print("NO")
        exit(0)

for i in result:
    print(i)