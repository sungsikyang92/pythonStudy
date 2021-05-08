h, w = map(float, input().split())
sw = (h - 100) * 0.9
bmi = (w - sw) * 100 / sw
if bmi <= 10:
    print("정상")
elif 10 < bmi <= 20:
    print("과체중")
else:
    print("비만")