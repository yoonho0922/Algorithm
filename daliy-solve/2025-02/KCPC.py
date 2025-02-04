# https://www.acmicpc.net/problem/3758

import sys
readline = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 팀 수, 문제 수, 우리 팀, 로그 수
    N, M, my_team, L = map(int, input().split())

    # 팀당 문제 득점
    question_scores = [[0] * (M + 1) for _ in range(N + 1)]
    # 시도 횟수
    tries = [0] * (N + 1)
    # 마지막 제출
    lasts = [10000] * (N + 1)

    # 로그 입력
    for i in range(L):
        # 팀, 문제, 점수
        team, question, score = map(int, readline().split())
        question_scores[team][question] = max(question_scores[team][question], score)
        tries[team] += 1
        lasts[team] = i

    # 순위 판단 배열
    results = []
    for i in range(1, N + 1):
        # 점수 총합, 시도 횟수, 마지막 제출
        results.append([sum(question_scores[i]), tries[i], lasts[i], i])

    results.sort(key=lambda x: [-x[0], x[1], x[2]])

    for i in range(1, N + 1):
        if results[i - 1][3] == my_team:
            print(i)
            break