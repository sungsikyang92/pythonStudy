w = input()
left_count = 0
right_count = 0
for x in range(len(w)):
    if w[x]=="(":
        left_count += 1
    else:
        right_count += 1
print(left_count, right_count)