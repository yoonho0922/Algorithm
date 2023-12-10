import sys
sys.setrecursionlimit(999999999)
readline = sys.stdin.readline

def dfs1(cur):
    visited1[cur] = True
    for next in G[cur]:
        if not visited1[next]:
            dfs1(next)
    s.append(cur)

def dfs2(cur):
    visited2[cur] = True
    scc.append(cur)
    for next in G_rev[cur]:
        if not visited2[next]:
            dfs2(next)

V, E = map(int, readline().split())
G = [[] for _ in range(V+1)]
G_rev = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, readline().split())
    G[a].append(b)
    G_rev[b].append(a)

visited1 = [False]*(V+1)
visited2 = [False]*(V+1)
s = []
SCC = []

for i in range(1, V+1):
    if not visited1[i]:
        dfs1(i)

while s:
    x = s.pop()
    if not visited2[x]:
        scc = []
        dfs2(x)
        scc.sort()
        SCC.append(scc)

SCC.sort()

print(len(SCC))
for scc in SCC:
    print(*scc, -1)