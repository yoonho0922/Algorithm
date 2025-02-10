# 시간초과

import sys
readline = sys.stdin.readline

def check(s, e):
    if (s-e+1)%2 == 0:
        mid = (s+e)//2

        for i in range(s, mid):
            # print(i, nums[i], nums[e-i])
            if nums[i] != nums[e-i]:
                return False
    else:
        mid = (s+e)//2

        for i in range(s, mid):
            # print(i, nums[i], nums[e+1-i])
            if nums[i] != nums[e-i]:
                return False

    return True

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    s, e = map(int, readline().split())

    if check(s-1, e-1):
        print('YES')
    else:
        print('NO')
