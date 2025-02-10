# https://www.acmicpc.net/problem/1655

import heapq
import sys
readline = sys.stdin.readline

N = int(input())
left_q = [] # max heap
right_q = [] # min heap

for i in range(N):
    x = int(readline())

    if i%2==0:
        # left 크기 늘리기
        if not right_q:
            left_q.append(-x)
        else:
            right_min = right_q[0]

            if x <= right_min:
                heapq.heappush(left_q, -x)
            else:
                # 오른쪽 가장 작은 값을 왼쪽 가장 큰 값으로 옮김
                heapq.heappop(right_q)
                heapq.heappush(left_q, -right_min)

                # 오른쪽에 푸시
                heapq.heappush(right_q, x)

    else:
        # right 크기 늘리기 (right를 넣는 시점에 left는 무조건 한 개 이상임)

        left_max = -left_q[0]

        if x >= left_max:
            heapq.heappush(right_q, x)
        else:
            # 왼쪽의 가장 큰 값을 오른쪽의 가장 작은 값으로 옮김
            heapq.heappop(left_q)
            heapq.heappush(right_q, left_max)

            # 왼쪽에 푸시
            heapq.heappush(left_q, -x)

    # print([-x for x in left_q[::-1]], right_q)
    print(-left_q[0])