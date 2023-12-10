
def dfs(x):
    visited[x] = True
    s.append(x)
    parent = x

    for next in G[x]:
        if not visited[next]: # 방문하지 않았다면
            parent = min(parent, dfs(next))
        elif not finished[next]: # dfs 처리 중이라면
            parent = min(parent, next)

    if parent == x: # 자기자신이 부모라면
        scc = []
        while True:
            t = s.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent


N = 11
G = [[] for _ in range(N+1)]
G[1].append(2)
G[2].append(3)
G[3].append(1)
G[4].append(2)
G[4].append(5)
G[5].append(7)
G[6].append(5)
G[7].append(6)
G[8].append(5)
G[8].append(9)
G[9].append(10)
G[10].append(11)
G[11].append(3)
G[11].append(8)

visited = [False]*(N+1)
finished = [False]*(N+1)
SCC = []
s = []

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

for scc in SCC:
    print(scc)
