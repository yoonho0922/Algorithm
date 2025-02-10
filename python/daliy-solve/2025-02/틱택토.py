# http://acmicpc.net/problem/7682

import sys
readline = sys.stdin.readline

def count_bingo(G, P):
    cnt = 0
    for i in range(3):
        # 세로
        if G[i] == G[i+3] == G[i+6] == P:
            cnt += 1
        # 가로
        if G[i*3] == G[i*3 + 1] == G[i*3 + 2] == P:
            cnt += 1
    # 대각선
    if G[0] == G[4] == G[8] == P:
        cnt += 1
    if G[2] == G[4] == G[6] == P:
        cnt += 1
    return cnt


def solution(G):
    x_n = G.count("X")
    o_n = G.count("O")
    x_win = count_bingo(G, "X")
    o_win = count_bingo(G, "O")
    if x_win + o_win == 0 and (x_n, o_n) == (5, 4):
        return "valid"
    elif x_win > 0 and o_win == 0 and (x_n == o_n + 1):
        return "valid"
    elif x_win == 0 and o_win > 0 and (x_n == o_n):
        return "valid"
    return "invalid"


while True:
    line = readline().strip()
    if line == "end":
        break
    else:
        print(solution(line))
