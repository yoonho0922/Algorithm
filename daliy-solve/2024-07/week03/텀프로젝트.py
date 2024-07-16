# https://www.acmicpc.net/problem/9466

import sys

sys.setrecursionlimit(100000)
readline = sys.stdin.readline


def dfs(X):
    visited[X] = True

    # 자기자신과 팀
    if G[X] == X:
        return 1

    if visited[G[X]]:
        if G[X] in cycle:
            return len(cycle) - cycle.index(G[X])
        else:
            return 0
    else:
        cycle.append(G[X])
        return dfs(G[X])

T = int(input())
for _ in range(T):
    N = int(readline())
    G = [0] + list(map(int, readline().split()))

    enrolled = 0
    visited = [False] * (N+1)

    for i in range(1, N+1):
        if not visited[i]:
            cycle = [i]
            enrolled += dfs(i)

    print(N - enrolled)