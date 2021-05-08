n = int(input())
nn = ' '
if n % 10 == 1:
    nn = str(n) + "st"
    if n == 11:
        nn = str(n) + "th"
elif n % 10 == 2:
    nn = str(n) + "nd"
    if n == 12:
        nn = str(n) + "th"
elif n % 10 == 3:
    nn = str(n) + "rd"
    if n == 13:
        nn = str(n) + "th"
else:
    nn = str(n) + "th"
print(nn)