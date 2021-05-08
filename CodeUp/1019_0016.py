yy, mm, dd = input().split(".")
print("%04d" %int(yy), end=".")
print("%02d" %int(mm), end=".")
print("%02d" %int(dd))