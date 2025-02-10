# ATM
# https://www.acmicpc.net/problem/11399

import sys
readline = sys.stdin.readline


N = int(readline())
P = list(map(int, readline().split()))


def solve():
    result = 0
    P.sort()

    for i in range(N):
        result += sum(P[0:i+1])

    print(result)

solve()
