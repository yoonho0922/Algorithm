import heapq


def solution(h, K):
    answer = 0
    heapq.heapify(h)

    while len(h) > 1 and h[0] < K:
        food1 = heapq.heappop(h)
        food2 = heapq.heappop(h)
        heapq.heappush(h, food1 + 2 * food2)
        answer += 1

    if h[0] < K:
        answer = -1

    return answer