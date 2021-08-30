from collections import deque
import sys
readline = sys.stdin.readline

def init():
    g = [[] for _ in range(N+1)]
    ind = [0]*(N+1)

    for i in range(N):
        for j in range(i+1, N):
            g[rank[i]].append(rank[j])
            ind[rank[j]] += 1

    return g, ind

def convert(a, b):
    # a->b convert to b->a
    for i in range(len(G[a])):
        if G[a][i] == b:
            G[a].pop(i)
            break
    G[b].append(a)

    inDegree[a] += 1
    inDegree[b] -= 1

def topology():
    q = deque()
    result = []

    for i in range(1, N+1):
        if inDegree[i]==0:
            q.append(i)

    for _ in range(N):
        if len(q)==0:
            print("IMPOSSIBLE")
            return

        cur = q.popleft()
        result.append(cur)

        for next in G[cur]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                q.append(next)

    print(*result)

    
T = int(readline())
for _ in range(T):
    N = int(readline())
    rank = list(map(int, readline().split()))

    G, inDegree = init()

    M = int(readline())
    for _ in range(M):
        x, y = map(int, readline().split())
        if y in G[x]: # if x->y
            convert(x, y)
        else:
            convert(y, x)

    topology()