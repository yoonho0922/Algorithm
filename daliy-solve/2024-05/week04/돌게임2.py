# https://acmicpc.net/problem/9656

N = int(input())
if N==1:
    print('CY')
    exit()

# True -> SK, False -> CY
dp = [False]*(N+1)
dp[0], dp[2] = True, True

for i in range(3, N+1):
    dp[i] = (not dp[i - 1]) or (not dp[i - 3])

if dp[N]:
    print('SK')
else:
    print('CY')