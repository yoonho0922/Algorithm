# https://www.acmicpc.net/problem/9017

MAX_TEAMS = 200


def solution(teams):
    # 팀별 완주자 파악
    counts = [0] * (MAX_TEAMS + 1)

    for team in teams:
        counts[team] += 1

    # 점수 집계
    scores = [[] for _ in range(MAX_TEAMS + 1)]
    seq = 1

    for team in teams:
        if counts[team] >= 6:
            scores[team].append(seq)
            seq += 1

    # 순위 판별
    win_team = 0
    win_score = 1000 * 1000
    win_fifth = 1000

    for team in range(1, MAX_TEAMS + 1):
        if scores[team]:
            cur_score = sum(scores[team][:4])
            cur_fifth = scores[team][4]
            if (cur_score < win_score) or (cur_score == win_score and cur_fifth < win_fifth):
                win_team = team
                win_score = cur_score
                win_fifth = cur_fifth

    return win_team


T = int(input())
for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    print(solution(teams))
