# https://www.acmicpc.net/problem/2960

N, K = map(int, input().split())

check = [False] * (N + 1)
cnt, ans = 0, 0

for i in range(2, N+1):
    if check[i]:
        continue
    for j in range(i, N+1, i):
        if not check[j]:
            check[j] = True
            cnt += 1
            if cnt == K:
                ans = j
print(ans)