from collections import deque


def solution(numbers, target):
    q = deque()
    q.append(numbers[0])
    q.append(-numbers[0])

    for i in range(1, len(numbers)):
        nexts = []
        while q:
            cur = q.popleft()
            nexts.append(cur + numbers[i])
            nexts.append(cur - numbers[i])
        if i == len(numbers) - 1:
            return nexts.count(target)
        for next in nexts:
            q.append(next)
