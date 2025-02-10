# https://www.acmicpc.net/problem/1026
# 보물

import sys
readline = sys.stdin.readline


N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

def solve():
    A.sort()
    B.sort(reverse=True)

    result = 0

    for i in range(N):
        result += A[i] * B[i]

    return result

print(solve())