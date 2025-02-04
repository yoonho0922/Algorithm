# https://www.acmicpc.net/problem/19637

import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
tags = []
conditions = []
for _ in range(N):
    tag, condition = readline().split()
    tags.append(tag)
    conditions.append(int(condition))
for _ in range(M):
    score = int(readline())
    left, right, idx = 0, N - 1, 0
    while left <= right:
        mid = (left + right) // 2
        if score > conditions[mid]:
            idx = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    print(tags[idx])