T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    nums.sort()

    for i in range(nums[0], nums[0]*nums[1]+1, nums[0]):
        if i%nums[1]==0:
            print(i)
            break