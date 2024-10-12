# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, trucks):
    q = deque([0] * bridge_length)
    time = 0
    now_weight = 0
    i = 0 # truck index

    while i < len(trucks):
        now_weight -= q.popleft()
        if i < len(trucks) and now_weight + trucks[i] <= weight:
            q.append(trucks[i])
            now_weight += trucks[i]
            i += 1
        else:
            q.append(0)
        time += 1

    # 마지막 트럭이 다리를 지나는 시간
    time += bridge_length

    return time