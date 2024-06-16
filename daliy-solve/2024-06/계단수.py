# https://www.acmicpc.net/problem/1562

DIVISION = 1_000_000_000

N = int(input())

dp = [[[0]*(1 << 10) for _ in range(10)] for _ in range(N+1)]

# 0을 제외하고 초기 값 셋팅
for i in range(1, 10):
    dp[1][i][1<<i] = 1

# 자리 수
for i in range(2, N+1):
    # 마지막 수
    for j in range(10):
        # 방문한 숫자의 조합
        for bit in range((1 << 10)):
            if j - 1 >= 0:
                dp[i][j-1][bit | 1 << (j-1)] += dp[i-1][j][bit] % DIVISION
            if j + 1 <= 9:
                dp[i][j+1][bit | 1 << (j+1)] += dp[i-1][j][bit] % DIVISION

ans = sum([dp[N][x][1023] for x in range(10)]) % DIVISION
print(ans)