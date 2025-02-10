# https://www.acmicpc.net/problem/2109

import heapq
from collections import deque

N = int(input())

if N == 0:
    print(0)
    exit()

# [강연료, 마감일]
requests: list = [list(map(int, input().split())) for _ in range(N)]

requests.sort(reverse=True, key=lambda x:x[1]) # 마감일이 높은 순으로 정렬
max_date = requests[0][1] # 가장 긴 마감일
request_q = deque(requests)
processing_q = []

answer = 0

for day in range(max_date, 0, -1):
    while request_q and request_q[0][1] == day:
        payment, _ = request_q.popleft()
        heapq.heappush(processing_q, -payment)

    if processing_q:
        payment = -heapq.heappop(processing_q)
        # print("info", payment)
        answer += payment

print(answer)