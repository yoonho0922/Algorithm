# https://www.acmicpc.net/problem/13904

import heapq
from collections import deque

N = int(input())
assignments = []

for _ in range(N):
    end_date, point = map(int, input().split())
    assignments.append([end_date, point])

assignments.sort(reverse=True) # 마감일의 역순으로 정렬
assignment_q = deque(assignments)
point_q = []
answer = 0
max_end_date = assignments[0][0] # 가장 긴 마감일

for day in range(max_end_date, 0, -1):
    # 해당  날짜에 처리할 수 있는 과제를 모두 큐에 담는다.
    while assignment_q and assignment_q[0][0] == day:
        end_date, point = assignment_q.popleft()
        heapq.heappush(point_q, -point)

    # 해당 날짜에 가장 점수가 높은 과제를 처리한다.
    if point_q:
        point = -heapq.heappop(point_q)
        answer += point

print(answer)
