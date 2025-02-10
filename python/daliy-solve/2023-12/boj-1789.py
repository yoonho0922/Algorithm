# https://www.acmicpc.net/problem/1789
# 수들의 합

import sys
readline = sys.stdin.readline

N = int(readline())

def solve():
    for i in range(2, sys.maxsize):
        if (i*(i+1)/2) > N:
            return i-1

print(solve())