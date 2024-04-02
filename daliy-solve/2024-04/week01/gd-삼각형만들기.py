# https://www.acmicpc.net/problem/1448

import sys
readline = sys.stdin.readline

N = int(readline())
nums = list(int(readline()) for _ in range(N))

nums.sort(reverse=True)

for i in range(N-2):
    if nums[i] < nums[i+1] + nums[i+2]:
        print(nums[i]+nums[i+1]+nums[i+2])
        break
else:
    print(-1)