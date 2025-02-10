# https://www.acmicpc.net/problem/12852

from collections import deque


def get_trace(visited_from, trace, target):
    now_step = trace[0]
    if now_step == target:
        return trace

    next_step = visited_from[now_step]

    return get_trace(visited_from, [next_step] + trace,target)

def bfs(N):
    q = deque()
    visited_from = [-1] * (N+1)

    visited_from[N] = 0
    q.append(N)
    count = -1

    while q:
        count += 1

        for _ in range(len(q)):
            now = q.popleft()

            if now == 1:
                print(count)
                for t in get_trace(visited_from, [1], N):
                    print(t,end=' ')

                return

            if now%3==0 and visited_from[now//3] == -1:
                q.append(now//3)
                visited_from[now//3] = now
            if now%2==0 and visited_from[now//2] == -1:
                q.append(now//2)
                visited_from[now//2] = now
            if visited_from[now-1] == -1:
                q.append(now-1)
                visited_from[now-1] = now


N = int(input())


bfs(N)