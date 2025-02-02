# https://www.acmicpc.net/problem/9017

import sys
readline = sys.stdin.readline


def completes(teams):
    is_complete = [False] * 201
    count = dict()
    for team in teams:
        if count.get(team):
            count[team] += 1
        else:
            count[team] = 1
        if count[team] >= 6:
            is_complete[team] = True
    return is_complete


def solution(teams: list):
    is_complete = completes(teams)
    # 팀 번호 : [점수, 마지막 도착]
    candidates = dict()
    score = 1
    for team in teams:
        if is_complete[team]:
            if candidates.get(team):
                candidates[team].append(score)
            else:
                candidates[team] = [score]
            score += 1


    winner = list(candidates.keys())[0]
    winner_score = sum(candidates[winner][:4])
    winner_last = candidates[winner][4]

    for team, scores in candidates.items():
        total_score = sum(scores[:4])
        if (total_score < winner_score) or (total_score == winner_score and scores[4] < winner_last):
            winner = team
            winner_score = total_score
            winner_last = scores[4]

    return winner



T = int(input())
for _ in range(T):
    _ = int(readline())
    teams = list(map(int, input().split()))
    print(solution(teams))
