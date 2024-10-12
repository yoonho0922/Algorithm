# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    total_time = len(prices) - 1
    answer = [-1] * len(prices)
    stack = [] # (price, time)

    for now_time, p in enumerate(prices):
        # 스택의 값이 증가하지 않도록 유지
        while stack and p < stack[-1][0]:
            price, time = stack.pop()
            answer[time] = now_time - time

        stack.append((p, now_time))

    # 스택에 남은 값들을 계산
    while stack:
        price, time = stack.pop()
        answer[time] = total_time - time

    return answer