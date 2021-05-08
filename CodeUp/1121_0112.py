sec = int(input())
min = 0
if sec >= 60:
    min = sec // 60
    sec = sec - (min * 60)

print(min, sec)