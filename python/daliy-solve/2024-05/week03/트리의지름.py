# https://www.acmicpc.net/problem/1167

from collections import deque
import sys
readline = sys.stdin.readline


def getFarthest(start):
    q = deque()
    visited = [False] * (V+1)

    q.append([start, 0])
    visited[start] = True

    dist = 0
    farthest = start

    while q:
        now, now_dist = q.popleft()

        for next, cost in G[now]:
            if visited[next]:
                continue

            next_dist = now_dist + cost

            q.append([next, next_dist])
            visited[next] = True

            # 가장 멀리있는 정점 갱신
            if next_dist > dist:
                dist = next_dist
                farthest = next

    return farthest, dist


V = int(input())
G = [[] for _ in range(V+1)]

for  _ in range(V):
    row = list(map(int, input().split()))
    start = row[0]
    i = 1
    while row[i] != -1:
        end, cost = row[i], row[i+1]
        G[start].append([end, cost])
        i += 2

# 임의의 정점에서 가장 멀리 떨어진 정점 A는 지름의 양끝 정점 중 하나임
A, _ = getFarthest(1)

# 지름 구하기
_, ans = getFarthest(A)

print(ans)
