from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    N = len(truck_weights)

    i = 0
    truck_time = [0] * N
    cur_weight = 0
    bridge = deque()

    # 마지막트럭이 다리를 통과할 때까지 반복
    while truck_time[N - 1] < bridge_length:

        # 다리의 무게를 초과하지 않으면 트럭을 보냄
        if i<N and cur_weight + truck_weights[i] <= weight :
            cur_weight += truck_weights[i]
            bridge.append(i)
            i += 1

        answer += 1

        # 현재 다리에 있는 트럭을 확인
        complete = False
        for t in bridge:
            truck_time[t] += 1
            # 시간이 지나면 다리 정보를 갱신함
            if truck_time[t] >= bridge_length:
                complete = True
                cur_weight -= truck_weights[t]
        if complete:
            bridge.popleft()
        print(answer, truck_time)
    return answer + 1

print(solution(100,	100,	[10,10,10,10,10,10,10,10,10,10]))