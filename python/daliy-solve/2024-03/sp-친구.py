# https://www.acmicpc.net/problem/1058

N = int(input())
friends = [list(input()) for _ in range(N)]
connected = [[0] * N for _ in range(N)]

# 플로이드워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                connected[i][j] = 1

result = 0

for i in range(N):
    result = max(result, sum(connected[i]))

print(result)
