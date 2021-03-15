import sys
readline = sys.stdin.readline
N = int(readline())
nums = [0]*10001
for _ in range(N):
    nums[int(readline())] += 1
for i in range(len(nums)):
    for j in range(nums[i]):
        print(i)