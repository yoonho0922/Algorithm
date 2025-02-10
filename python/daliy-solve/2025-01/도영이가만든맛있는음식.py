# https://www.acmicpc.net/problem/2961


def backtracking(acidity, acerbity, depth):
    if depth > 0:
        global answer
        answer = min(answer, abs(acidity - acerbity))
    for i in range(depth, N):
        backtracking(acidity * foods[i][0], acerbity + foods[i][1], i + 1)


N = int(input())
foods = [list(map(int, input().split())) for _ in range(N)]
answer = abs(foods[0][1] - foods[0][0])

# 신맛은 곱, 쓴맛은 합
backtracking(1, 0, 0)

print(answer)