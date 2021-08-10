nums = list(map(int, input().split()))
nums.sort()
g_factor = 1
for i in range(2, nums[1]+1):
    if nums[0]%i==0 and nums[1]%i==0:
        g_factor=i
print(g_factor)
for i in range(nums[0], nums[0]*nums[1]+1, nums[0]):
    if i%nums[1]==0:
        print(i)
        break