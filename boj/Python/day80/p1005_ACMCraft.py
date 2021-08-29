from collections import deque
import sys
readline = sys.stdin.readline

def topology():
    q = deque()
    result = [0]*(N+1)

    for i in range(1, N+1):
        if inDegree[i]==0:
            q.append(i)

    for _ in range(N):

        cur = q.popleft()
        result[cur] += D[cur]

        if cur==W:
            return result[cur]

        for next in G[cur]:
            inDegree[next] -= 1
            # 직적에 가장오래걸리는 건설시간
            result[next] = max(result[next], result[cur])
            if inDegree[next] ==0:
                q.append(next)


T = int(readline())
for _ in range(T):
    N, K = map(int, readline().split())
    D = [0] + list(map(int, readline().split()))
    G = [[] for _ in range(N+1)]
    inDegree = [0]*(N+1)
    for _ in range(K):
        X, Y = map(int, readline().split())
        G[X].append(Y)
        inDegree[Y] += 1
    W = int(readline())

    print(topology())