# https://www.acmicpc.net/problem/12919

from collections import deque, defaultdict


def bfs(S, E):
    q = deque()
    # visited = defaultdict(bool)

    q.append(E)
    # visited[E] = True

    while q:
        now = q.popleft()

        if now == S:
            return 1

        if now[0] == 'B':
            next = ''.join(reversed(now[1:]))
            q.append(next)
            if len(next) >= len(S):
                q.append(next)
        if now[-1] == 'A':
            next = now[:-1]
            if len(next) >= len(S):
                q.append(next)

    return 0

S = input()
E = input()

print(bfs(S, E))