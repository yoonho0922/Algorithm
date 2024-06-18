# https://yabmoons.tistory.com/188

import sys
readline = sys.stdin.readline

def find_parent(x):
    if parents[x] == x:
        return parents[x]
    return find_parent(parents[x])

def union(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)
    if root_a < root_b:
        parents[root_b] = root_a
    else:
        parents[root_a] = root_b


N, M = map(int, input().split())
G = [list(map(int,readline().split())) for _ in range(M)]
parents = [i for i in range(N+1)]

G.sort(key=lambda x : x[2])

ans = 0
max_cost = 0

for s, e, cost in G:
    if find_parent(s) != find_parent(e):
        union(s, e)
        ans += cost
        max_cost = cost

# 스패닝 트리 edge 중 가장 큰 edge 제외
print(ans - max_cost)