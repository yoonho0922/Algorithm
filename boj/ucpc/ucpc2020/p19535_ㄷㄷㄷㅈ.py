import sys
from collections import deque
readline = sys.stdin.readline

# Depth 계산
def bfs(du, ga):
    q = deque([1])
    depth[1] = 0

    while q:
        cur = q.popleft() # current node

        # count du
        if depth[cur] >= 3:
            # print('du type 1 : ', du)
            du += 1

        if len(G[cur]) >= 2:
            for child in G[cur]:
                if len(G[child]) > 0:
                    du += len(G[child]) * (len(G[cur]) - 1)
                    # print('du type 2 : ', du)

        # count ga
        if depth[cur] >= 1 and len(G[cur]) >= 2:
            m = len(G[cur]) # 자식의 수
            ga += m * (m - 1) // 2 # m combination 2

        if len(G[cur]) >= 3:
            m = len(G[cur]) # 자식의 수
            ga += m * (m-1) * (m-2) // 6 # m combination 3

        for next in G[cur]:
            depth[next] = depth[cur] + 1
            q.append(next)

    return du, ga


N = int(input())
G = [[] for _ in range(N+1)] # 1~N 노드
depth = [-1 for _ in range(N+1)] # 1~N 노드의 깊이 루트노드 = 0

for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)

du, ga = bfs(0, 0)

if du > ga*3:
    print('D')
elif du < ga*3:
    print('G')
elif du == ga*3:
    print('DUDUDUNGA')
print(du, ga)