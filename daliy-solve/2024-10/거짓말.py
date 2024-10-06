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
# 미리 알고 있는 사람 입력
is_know = [False] * (N + 1)
for f in list(map(int, input().split()))[1:]:
    is_know[f] = True

# 파티 참여자 입력
G = [set() for _ in range(N + 1)]
parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for participant in party:
        G[participant].update(party)

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