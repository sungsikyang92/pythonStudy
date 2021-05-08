text = input()
password = ''
for x in range(len(text)):
    if text[x] == ' ':
        password += text[x]
    elif ord(text[x]) > 119:
        if text[x] == 'x':
            password += 'a'
        elif text[x] == 'y':
            password += 'b'
        elif text[x] == 'z':
            password += 'c'
    else:
        code = ord(text[x]) + 3
        password += chr(code)
print(password)