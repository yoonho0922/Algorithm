from collections import deque
import sys

readline = sys.stdin.readline


def topology():
    q = deque()
    result = []

    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)

    for i in range(N):

        cur = q.popleft()
        result.append(cur)

        for next in G[cur]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                q.append(next)

    print(' '.join(list(map(str, result))))


N, M = map(int, readline().split())
G = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, readline().split())
    G[a].append(b)
    inDegree[b] += 1

topology()
