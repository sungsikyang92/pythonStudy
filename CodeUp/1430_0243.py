n = int(input())
nums = list(map(int, input().split()))
q_n = int(input())
questions = list(map(int, input().split()))

for y in range(n):
    for x in range(len(questions)):
        if questions[x] == nums[y]:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()