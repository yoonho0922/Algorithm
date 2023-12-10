from collections import deque


def search(G, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()
        for next in range(len(G[cur])):
            if G[cur][next] == 1 and not visited[next]:
                q.append(next)
                visited[next] = True
    return visited


def solution(N, computers):
    answer = 0
    visited = [False] * N

    for i in range(N):
        if not visited[i]:
            visited = search(computers, visited, i)
            answer += 1

    return answer