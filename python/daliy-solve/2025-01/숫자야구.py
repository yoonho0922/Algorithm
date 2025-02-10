# https://www.acmicpc.net/problem/2503

answer = 0

N = int(input())
question_and_results = [list(map(int, input().split())) for _ in range(N)]

def check(num: str):
    for qr in question_and_results:
        question = str(qr[0])
        strike, ball = 0, 0

        for i in range(3):
            if num[i] in question:
                if num[i] == question[i]:
                    strike += 1
                else:
                    ball += 1

        if not (strike == qr[1] and ball == qr[2]):
            return False

    # 모두 충족 시
    return True

def backtracking(num: str, visited: list):
    if len(num) == 3:
        if check(num):
            global answer
            answer += 1
        return

    for i in range(1, 10):
        if not visited[i]:
            visited[i] = True
            backtracking(str(i) + num, visited)
            visited[i] = False

visited = [False] * 10
backtracking("", visited)
print(answer)