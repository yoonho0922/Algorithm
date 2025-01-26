# https://www.acmicpc.net/problem/20437

import sys
readline = sys.stdin.readline


def solution(s: str, k: int):
    shortest = len(s) + 1
    longest = 1

    d = dict()
    for index, c in enumerate(s):
        if d.get(c):
            d[c].append(index)
        else:
            d[c] = [index]

    satisfies = []

    # 3번을 만족하는 가장 짧은 문자열 길이 구하기
    for key, value in d.items():
        if len(value) >= k:
            for i in range(k - 1, len(value)):
                start = value[i - k + 1]
                end = value[i]
                satisfies.append([start, end])
                shortest = min(shortest, end - start + 1)
                longest = max(longest, end - start + 1)

    if shortest <= len(s):
        print(shortest, longest)
    else:
        print(-1)

T = int(readline())
for _ in range(T):
    S = readline()
    K = int(readline())
    solution(S, K)