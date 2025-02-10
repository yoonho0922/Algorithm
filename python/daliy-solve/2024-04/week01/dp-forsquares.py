# https://www.acmicpc.net/problem/17626

N = int(input())
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    j = int(i**0.5)
    ans = 100000
    while j>=1:
        if j*j == i:
            ans = 1
            break

        ans = min(ans, dp[j*j] + dp[i - j*j])
        j -=1
    dp[i] = ans

# print(dp)
print(dp[N])