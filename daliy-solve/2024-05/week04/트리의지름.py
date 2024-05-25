# https://www.acmicpc.net/problem/1967

from collections import deque
import sys
readline = sys.stdin.readline

def get_farthest(G, N, S):
    q = deque()
    visited = [False] * (N+1)

    q.append([S,0])
    visited[S] = True

    max_dist = 0
    farthest = S

    while q:
        now, dist = q.popleft()

        if dist > max_dist:
            farthest = now
            max_dist = dist

        for next, next_cost in G[now]:
            if not visited[next]:
                visited[next] = True
                q.append([next, dist+next_cost])

    return [farthest, max_dist]



N = int(input())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    G[parent].append([child, weight])
    G[child].append([parent, weight])

edge_node, _ = get_farthest(G, N, 1)
_, diameter = get_farthest(G, N, edge_node)

print(diameter)