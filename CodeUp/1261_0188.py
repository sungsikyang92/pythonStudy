nums = list(map(int, input().split()))
nums.sort()
isFifth = False
for x in nums:
    if x % 5 == 0:
        print(x)
        isFifth = True
        break
if isFifth == False:
    print(0)