from collections import deque


def topologySort():
    q = deque()

    for i in range(1, N + 1):
        if (inDegree[i] == 0):
            q.append(i)

    for i in range(1, N+1):
        if len(q) == 0:
            print("cycle")
            return

        cur = q.popleft()
        result[i] = cur

        for j in range(len(G[cur])):
            next = G[cur][j]
            inDegree[next] -= 1
            if inDegree[next]==0:
                q.append(next)

    for i in range(1, N+1):
        print(result[i], end=' ')

N = 7
G = [[] for _ in range(N+1)]
inDegree = [0] * (N + 1)
result = [0] * (N + 1)

G[1].append(2)
G[1].append(5)
G[2].append(3)
G[3].append(4)
G[4].append(6)
G[5].append(6)
G[6].append(7)
inDegree[2]=1
inDegree[3]=1
inDegree[4]=1
inDegree[5]=1
inDegree[6]=2
inDegree[7]=1


topologySort()
