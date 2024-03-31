# https://www.acmicpc.net/problem/1890

from collections import deque
import sys
readline = sys.stdin.readline

dy = [0,1]
dx = [1,0]


def solution(N, G):
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1

    for cy in range(N):
        for cx in range(N):
            if G[cy][cx] == 0:
                continue

            for i in range(2):
                ny = cy + dy[i] * G[cy][cx]
                nx = cx + dx[i] * G[cy][cx]

                if 0<=ny<N and 0<=nx<N:
                    dp[ny][nx] += dp[cy][cx]

    print(dp[N-1][N-1])

N = int(input())
G = [list(map(int, readline().split())) for _ in range(N)]

solution(N, G)