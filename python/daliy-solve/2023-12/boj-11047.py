# https://www.acmicpc.net/problem/11047
# 동전0

import sys
readline = sys.stdin.readline


N, K = map(int, readline().split())
coins = [] # min = 1
for i in range(N):
    coins.append(int(readline()))

def solve():
    coins.sort(reverse=True)
    remainder = K
    count = 0

    for i in range(K//coins[-1]):
        count += remainder // coins[i]
        remainder %= coins[i]
        if remainder==0:
            return count

    return -1

print(solve())