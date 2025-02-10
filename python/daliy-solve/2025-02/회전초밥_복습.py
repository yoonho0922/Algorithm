# https://www.acmicpc.net/problem/2531

import sys
readline = sys.stdin.readline

# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split())
nums = [int(readline()) for _ in range(N)]
nums += nums
answer = 0
for i in range(N):
    answer = max(answer, len(set(nums[i:i+k] + [c])))
print(answer)
