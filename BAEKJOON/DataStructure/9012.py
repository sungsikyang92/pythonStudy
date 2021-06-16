import sys

inp = int(input())

for _ in range(inp):
    inp_ps = str(sys.stdin.readline().strip().split())
    stack = []
    check = 0
    for ps in inp_ps:
        if ps == "(":
            stack.append(ps)
        elif ps == ")":
            if len(stack) == 0:
                print("NO")
                check = 1
                break
            else:
                stack.pop(-1)

    if len(stack) != 0 and check == 0: print("NO")
    elif len(stack) == 0 and check == 0: print("YES")