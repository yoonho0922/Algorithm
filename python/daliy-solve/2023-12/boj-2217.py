# https://www.acmicpc.net/problem/2217
# 로프

import sys

readline = sys.stdin.readline

N = int(readline())
ropes = []
for _ in range(N):
    ropes.append(int(readline()))


def solve():
    ropes.sort(reverse=True)
    result = 0
    for i in range(N):
        result = max(result, ropes[i] * (i + 1))
    return result

print(solve())