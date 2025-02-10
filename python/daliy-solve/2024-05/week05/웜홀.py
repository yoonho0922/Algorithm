# https://www.acmicpc.net/problem/1865

import sys
readline = sys.stdin.readline

INF = 1e9

def check_cycle(N, S, G, visited):
    dists = [INF] * (N+1)

    visited[S] = True
    dists[S] = 0

    for i in range(N):
        for now in range(1, N+1):
            for next, cost in G[now]:
                new_dist = dists[now] + cost
                if dists[next] > new_dist:
                    dists[next] = new_dist
                    visited[next] = True

                    # N 번째 검사에서 경로가 갱신되면 음수 사이클 존재
                    if i == N-1:
                        return True
    return False

T = int(input())

for _ in range(T):
    N, M, W = map(int, readline().split())
    G = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    dists = [INF] * (N+1)

    for _ in range(M):
        S, E, T = map(int, input().split())
        G[S].append([E, T])
        G[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        G[S].append([E, -T])

    for i in range(1, N+1):
        if not visited[i] and check_cycle(N, i, G, visited):
            print('YES')
            break
    else:
        print('NO')


