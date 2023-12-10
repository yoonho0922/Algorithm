from collections import deque

N = int(input())
d = [-1] * (N+1)

def bfs(start):
    q = deque()
    q.append(start)
    d[start] = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == 1:
                return d[cur]

            if cur%3 == 0 and 0<cur:
                next = cur//3
                if d[next] == -1:
                    q.append(next)
                    d[next] = d[cur] + 1
            if cur%2 == 0 and 0<cur:
                next = cur//2
                if d[next] == -1:
                    q.append(next)
                    d[next] = d[cur] + 1
            next = cur - 1
            if d[next] == -1:
                q.append(next)
                d[next] = d[cur] + 1

print(bfs(N))