# https://www.acmicpc.net/problem/2012

import sys
readline = sys.stdin.readline

N = int(input())
S = [int(readline()) for _ in range(N)]
S.sort()

total = 0

for i in range(1, N + 1):
    total += abs(i - S[i-1])

print(total)