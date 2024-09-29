# https://www.acmicpc.net/problem/9019

from collections import deque

THRESHOLD = 10_000
NOT_VISITED = "NONE"


def do_l(now_value: int):
    s = str(now_value)
    s = "0" * (4 - len(s)) + s # s는 항상 네 자리다.
    return int(s[1:] + s[0])

def do_r(now_value: int):
    s = str(now_value)
    s = "0" * (4 - len(s)) + s
    return int(s[3] + s[:3])


def bfs(start, target):
    visited = [NOT_VISITED] * THRESHOLD
    q = deque()

    visited[start] = ""
    q.append(start)

    while q:
        now_value = q.popleft()
        if now_value == target:
            return visited[now_value]

        for method in ['D', 'S', 'L', 'R']:
            if method == 'D':
                next_value = (now_value * 2) % THRESHOLD
            elif method == 'S':
                next_value = now_value - 1 if now_value > 0 else THRESHOLD - 1
            elif method == 'L':
                next_value = do_l(now_value)
            elif method == 'R':
                next_value = do_r(now_value)
            else:
                raise Exception("정의되지 않은 연산입니다.")

            if visited[next_value] == NOT_VISITED:
                visited[next_value] = visited[now_value] + method
                q.append(next_value)



T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    answer = bfs(A, B)
    print(answer)

# # TEST
# a = int(input())
# print(do_r(a))