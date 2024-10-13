# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heappush, heappop
from collections import defaultdict

def clean(q, d, correction):
    # 최대힙일 경우 correction : -1
    while q and d[q[0] * correction] == 0:
        heappop(q)


def solution(operations):
    maxq = []
    minq = []
    d = defaultdict(int)

    for op in operations:
        cmd, num = op.split()
        # print(cmd, num)
        if cmd == "I": # 삽입
            d[int(num)] += 1
            heappush(maxq, -int(num))
            heappush(minq, int(num))
        else:
            if num == "1":
                clean(maxq, d, -1)
                if maxq:
                    element = -heappop(maxq)
                    d[element] -= 1
            else:
                clean(minq, d, 1)
                if minq:
                    element = heappop(minq)
                    d[element] -= 1

    clean(maxq, d, -1)
    clean(minq, d, 1)

    if maxq and minq:
        return [-maxq[0], minq[0]]
    else:
        return [0,0]