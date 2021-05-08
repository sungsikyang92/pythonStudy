word = input()

for x in range(len(word)):
    if word[x] == "t":
        print(x+1, end=" ")