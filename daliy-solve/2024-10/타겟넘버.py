# https://school.programmers.co.kr/learn/courses/30/lessons/43165#

answer = 0

def dfs(numbers, target, result: int, index: int):
    if index >= len(numbers):
        if result == target:
            global answer
            answer += 1
        return
    # 더하기
    dfs(numbers, target, result + numbers[index], index + 1)
    # 빼기
    dfs(numbers, target, result - numbers[index], index + 1)
    return

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer