# https://www.acmicpc.net/problem/1535

def dfs(start, life, joy):
    global ans
    ans = max(ans, joy)

    for i in range(start, N):
        if life - L[i] > 0:
            dfs(i + 1, life - L[i], joy + J[i])

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

ans = 0
dfs(0, 100, 0)

print(ans)