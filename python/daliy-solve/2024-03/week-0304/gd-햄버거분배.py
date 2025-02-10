# https://www.acmicpc.net/problem/19941

N, K = map(int, input().split())
S = input()
visited = [False]*N
cnt = 0


for i in range(N):
    if visited[i]:
        continue

    for j in range(i+1, min(i+K+1, N)):
        if not visited[j] and S[i] != S[j]:
            cnt += 1
            # print(i, visited[i], j, visited[j])
            visited[i], visited[j] = True, True
            break
# print(visited)
print(cnt)