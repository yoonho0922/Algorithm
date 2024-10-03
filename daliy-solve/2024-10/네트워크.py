# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def bfs(start, visited, computers, n):
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        now_computer = q.popleft()

        for next_computer in range(n):
            if (computers[now_computer][next_computer] == 1
                    and not visited[next_computer]):
                q.append(next_computer)
                visited[next_computer] = True



def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            answer += 1

    return answer