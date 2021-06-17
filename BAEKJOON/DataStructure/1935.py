inp = int(input())
equation = list(input())

num = []
for i in range(inp):
    num.append(input())

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(equation)):
    if equation[i].isalpha():
        equation[i] = num[alpha.index(equation[i])]

stack = []
for i in equation:
    if i.isdigit():
        stack.append(i)

    else:
        b = float(stack.pop())
        a = float(stack.pop())
        if i == "+":
            stack.append(a+b)
        elif i == "-":
            stack.append(a-b)
        elif i == "*":
            stack.append(a*b)
        elif i == "/":
            stack.append(a/b)

print('{0:.2f}'.format(stack[0]))