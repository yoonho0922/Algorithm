# https://www.acmicpc.net/problem/1043

from collections import deque

def bfs(G, is_know, visited, start):
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        now_human = q.popleft()
        for next_human in G[now_human]:
            if not visited[next_human]:
                is_know[next_human] = True
                visited[next_human] = True
                q.append(next_human)

# 기본 입력
N, M = map(int, input().split())
inputs = list(map(int, input().split()))
is_know = [False] * (N + 1)
for f in inputs[1:]:
    is_know[f] = True

G = [set() for _ in range(N + 1)]

# 파티 참여자 입력
parties = []
for _ in range(M):
    inputs = list(map(int, input().split()))
    parties.append(inputs[1:])
    participants = inputs[1:]
    for participant in participants:
        G[participant].update(participants)

# 진실 전파
visited = [False] * (N+1)
for i in range(1, N+1):
    if is_know[i]:
        visited[i] = True
        bfs(G, is_know, visited, i)


# 거짓말 파티 구하기
answer = 0
for party in parties:
    for human in party:
        if is_know[human]:
            break
    else:
        answer += 1
print(answer)