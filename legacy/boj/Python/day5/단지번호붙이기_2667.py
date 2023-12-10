def bfs(s):
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    num, q = 1, []
    G[s[0]][s[1]] = 0
    q.append(s)

    while q:
        curr = q.pop(0)
        # curr의 상하좌우 검사
        for i in range(4):
            ny = curr[0] + dy[i]
            nx = curr[1] + dx[i]
            # 범위를 넘지 않으면
            if 0<=ny<N and 0<=nx<N:
                # 방문하지 않았으면
                if G[ny][nx] == 1:
                    G[ny][nx] = 0
                    q.append([ny, nx])
                    num += 1
    # 단지내 집의 수 추가
    nums.append(num)


# 입력
N = int(input())
G = [[0]*N for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(N):
        G[i][j] = int(line[j])

total = 0 # 총 단지수
nums = [] # 각 단지내 집의 수

for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            total += 1
            bfs([i, j])
# 오름차순 정렬
nums.sort()
# 출력
print(total)
for num in nums:
    print(num)