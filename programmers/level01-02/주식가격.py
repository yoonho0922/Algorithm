def solution(prices):
    answer = []
    for i in range(len(prices)):
        day = 0
        for j in range(i + 1, len(prices)):
            day += 1
            if prices[j] < prices[i]:
                break
        answer.append(day)
    return answer