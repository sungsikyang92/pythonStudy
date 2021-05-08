n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
for x in range(len(nums)):
    print(nums[x], end=" ")