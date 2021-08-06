from collections import deque
import sys
readline = sys.stdin.readline


def bfs(s, depth):
    global du, ga

    q = deque()
    visited = [False] * (N + 1)

    visited[s] = True
    q.append(s)

    while q:
        cur = q.popleft()
        # get ga
        if len(G[cur]) >=3:
            m = len(G[cur])
            ga += m*(m-1)*(m-2)//6

        for next in G[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                # get du
                if len(G[cur]) >= 2 and len(G[next]) >= 2:
                    du += (len(G[cur]) - 1) * (len(G[next]) - 1)



N = int(readline())
G = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

du, ga, = 0, 0

bfs(1, 0)

if du == ga*3:
    print("DUDUDUNGA")
elif du > ga*3:
    print("D")
elif du < ga*3:
    print("G")