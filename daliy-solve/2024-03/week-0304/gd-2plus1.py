# https://www.acmicpc.net/problem/11508

import sys
readline = sys.stdin.readline

N = int(input())
A = [int(readline()) for _ in range(N)]

A.sort(reverse=True)

total = 0

for i in range(N):
    if i%3 != 2:
        total += A[i]

print(total)