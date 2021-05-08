string = input()
count = 0
for x in range(len(string)):
    if string[x:x+4] == "love":
        count += 1
print(count)