chicken, house = [], []

def minChicken(y, x):
    mc = 9999999
    for i in range(C):
        if visited[i]:
            cur_chicken = abs(y-chicken[i][0]) + abs(x-chicken[i][1])
            mc = min(mc, cur_chicken)
    return mc

def totalChicken():
    total = 0
    for h in house:
        total += minChicken(h[0],h[1])
    return total

def dfs(idx, depth):
    if depth == M:
        global ans
        tc = totalChicken()
        ans = min(ans, tc)
        return

    for i in range(idx, C):
        visited[i] = True
        dfs(i+1, depth+1)
        visited[i] = False


N, M = map(int, input().split())
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append([i, j])
        elif row[j] == 2:
            chicken.append([i, j])

C, H = len(chicken), len(house)
visited = [False]*C
ans = 999999999

dfs(0, 0)

print(ans)