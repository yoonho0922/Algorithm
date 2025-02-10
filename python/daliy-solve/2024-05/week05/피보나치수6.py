# https://www.acmicpc.net/problem/11444

from collections import defaultdict

NUMBER = 1_000_000_007


def pibo(k):
    if d[k]:
        return d[k]

    if k%2 == 0:
        d[k] = (pibo(k//2) * (pibo(k//2 + 1) + pibo(k//2 - 1))) % NUMBER
    else:
        d[k] = (pibo((k+1)//2) ** 2 + pibo((k-1)//2) ** 2) % NUMBER

    return d[k]


N = int(input())

d = defaultdict(int)
d[0], d[1], d[2] = 0, 1, 1

print(pibo(N))