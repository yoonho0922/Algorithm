# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from collections import deque

def solution(jobs):
    N = len(jobs)
    jobs = deque(sorted(jobs))
    hq = []
    t, ans = 0, 0

    for i in range(N):
        # 실행 후보 구하기
        while jobs:
            if jobs[0][0] > t:
                break
            job = jobs.popleft()
            heapq.heappush(hq, (job[1],job[0]))

        if hq:
            # 실행 후보가 있으면 실행하기
            processing_time, start = heapq.heappop(hq)
            t += processing_time
            ans += (t-start)
        else:
            # 실행 후보가 없으면 가장 빨리 실행할 수 있는 job 실행하기
            start, processing_time = jobs.popleft()
            t = start + processing_time
            ans += (processing_time)

    return ans//N