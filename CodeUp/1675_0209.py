text = input()
p = ''

for x in range(len(text)):
    if text[x] == ' ':
        p += text[x]
    elif text[x] == 'a':
        p += 'x'
    elif text[x] == 'b':
        p += 'y'
    elif text[x] == 'c':
        p += 'z'
    else:
        c = ord(text[x]) - 3
        p += chr(c)
print(p)