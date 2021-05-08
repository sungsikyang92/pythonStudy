nums = list(map(int, input().split()))
nums.sort()
if nums[2] < nums[0] + nums[1] :
    print("yes")
else:
    print("no")
