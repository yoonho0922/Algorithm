# https://www.acmicpc.net/problem/2720
# 세탁소 사장 동혁

import sys
readline = sys.stdin.readline

T = int(readline())

coin_types = [25, 10, 5, 1]

def solve(total):
    coin_counts = []

    for coin in coin_types:
        coin_counts.append(total//coin)
        total %= coin

    print(*coin_counts)

for _ in range(T):
    total = int(readline())
    solve(total)