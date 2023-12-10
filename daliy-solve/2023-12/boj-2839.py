# 설탕배달
# https://www.acmicpc.net/problem/2839

import sys


def solve(N):
    result = sys.maxsize
    for i in range(N // 5, -1, -1):
        after_minus = N - 5 * i
        if after_minus % 3 == 0:
            result = min(i + after_minus // 3, result)

    if result == sys.maxsize:
        print(-1)
    else:
        print(result)


N = int(input())
solve(N)
