# https://www.acmicpc.net/problem/1463

import collections

def get_least_count(N):
    dp = [0]*(N+1)

    q = collections.deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x%3 == 0 and dp[x//3] == 0:
            dp[x//3] = dp[x] + 1
            q.append(x//3)
        if x%2 == 0 and dp[x//2] == 0:
            dp[x//2] = dp[x] + 1
            q.append(x//2)
        if x-1 >= 1 and dp[x-1] == 0:
            dp[x-1] = dp[x] + 1
            q.append(x-1)

    return dp[1]


N = int(input())

print(get_least_count(N))