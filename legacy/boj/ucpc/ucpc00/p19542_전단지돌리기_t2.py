import sys
sys.setrecursionlimit(99999)
readline = sys.stdin.readline

def dfs(start):
    # leaf 노드인 경우
    if start!=S and len(G[start])==1:
        visited[start]=D
        return D

    val = 999999999999
    for next in G[start]:
        if visited[next]==-1:
            visited[next]=0
            c = max(dfs(next)-1, 0)
            # print(start, c)
            val = min(val, c)

    visited[start]=val
    return visited[start]

N, S, D = map(int, readline().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

visited=[-1]*(N+1)
visited[S]=0
dfs(S)

ans = 0
for i in range(1, N+1):
    if i!=S and visited[i] == 0:
        ans+=1

print(ans*2)