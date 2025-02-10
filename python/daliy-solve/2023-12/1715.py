# https://www.acmicpc.net/problem/1715
# 카드 정렬하기

import sys
import heapq
readline = sys.stdin.readline

N = int(readline())
card_heap = []

for _ in range(N):
    heapq.heappush(card_heap, int(readline()))

def solve():
    result = 0

    for i in range(1, N):
        fir = heapq.heappop(card_heap)
        sec = heapq.heappop(card_heap)

        heapq.heappush(card_heap, fir+sec)
        result += fir+sec

    print(result)

solve()