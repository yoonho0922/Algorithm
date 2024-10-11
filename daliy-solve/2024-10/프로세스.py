# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(prior, location):
    q = deque([(index, p) for index, p in enumerate(prior)])
    print(q)
    cnt = 1

    while q:
        process = q.popleft()
        if all(process[1] >= p[1] for p in q):
            if process[0] == location:
                return cnt
            cnt += 1
        else:
            q.append(process)

    return -1