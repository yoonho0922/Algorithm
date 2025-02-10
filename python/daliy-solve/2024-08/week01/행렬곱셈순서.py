# https://www.acmicpc.net/problem/11049

MAX_VALUE = 2 ** 31 - 1

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[MAX_VALUE] * N for _ in range(N)]

for i in range(N + 1):
    # i 번 째 대각선
    for j in range(N - i):
        # j 번 째 행
        if i == 0:
            dp[j][j + i] = 0
        elif i == 1:
            dp[j][j + 1] = matrix[j][0] * matrix[j][1] * matrix[j + 1][1]
        else:
            for k in range(j, j + i):
                dp[j][j + i] = min(
                    dp[j][j + i],
                    # j~k 행렬 곱의 최소값 + (k+1)~(j+i) 행렬 곱의 최소값 + (j행렬[0] * k행렬[1] * (j+i)행렬[1])
                    dp[j][k] + dp[k + 1][j + i] + (matrix[j][0] * matrix[k][1] * matrix[j + i][1])
                )

print(dp[0][N-1])
