# https://www.acmicpc.net/problem/13549

from collections import deque

MAX_LENGTH = 200000

def bfs(N, K):
    counts = [-1] * (MAX_LENGTH+1)
    q = deque()

    q.append(N)
    counts[N] = 0

    while q:
        now = q.popleft()

        # 0에서 시작하는 경우 예외 처리
        if now == 0:
            q.append(1)
            counts[1] = counts[now] + 1
            continue

        # 순간 이동
        teleport = now * 2
        while teleport <= MAX_LENGTH:
            if counts[teleport] == -1:
                q.append(teleport)
                counts[teleport] = counts[now]

            teleport *= 2

        # 걷기
        for d in [1, -1]:
            next = now + d
            if next <= MAX_LENGTH and counts[next] == -1:
                q.append(next)
                counts[next] = counts[now] + 1

    return counts[K]

N, K = map(int, input().split())


print(bfs(N, K))
