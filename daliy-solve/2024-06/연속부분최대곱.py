# https://www.acmicpc.net/problem/2670

import sys
readline = sys.stdin.readline

N = int(input())
nums = [float(readline()) for _ in range(N)]
dp = [nums[0]]

for i in range(1, N):
    if dp[i-1] <= 1:
        dp.append(nums[i])
    else:
        dp.append(dp[i-1] * nums[i])

print('%0.3f' % max(dp))