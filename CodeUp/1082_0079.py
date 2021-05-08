num = input()
num = int(num, 16)

for x in range(1, 16):
    print('%0X' %num, end="*")
    print('%0X' % x, end="=")
    print('%0X' %(num*x))