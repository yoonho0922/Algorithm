# 이코 p.298 서로소 집합

import sys

readline = sys.stdin.readline


def find_root(roots, x):
    if roots[x] != x:
        roots[x] = find_root(roots, roots[x])
    return roots[x]


def union(roots, a, b):
    a_root = find_root(roots, a)
    b_root = find_root(roots, b)

    if a_root < b_root:
        roots[b] = a_root
    else:
        roots[a] = b_root

N, M = map(int, input().split())
roots = [i for i in range(N+1)]

for _ in range(M):
    method, a, b = map(int, readline().split())

    if method == 0:
        union(roots, a, b)
    if method == 1:
        if find_root(roots, a) == find_root(roots, b):
            print('YES')
        else:
            print('NO')