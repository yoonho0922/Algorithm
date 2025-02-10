# https://www.acmicpc.net/problem/15684

def check_condition():
    for i in range(N):
        col = i
        for j in range(H):
            if col == 0:
                if G[j][col]:
                    col += 1
            elif col == N-1:
                if G[j][col-1]:
                    col -= 1
            else:
                if G[j][col]:
                    col += 1
                elif G[j][col-1]:
                    col -= 1
        if col != i:
            return False

    return True

def check_available(i, j):
    if j==0:
        return not G[i][j+1]
    else:
        return not G[i][j - 1] and not G[i][j + 1]

def dfs(start, cnt):
    global ans
    if check_condition():
        ans = min(ans, cnt)
        return
    if cnt == 3 or cnt >= ans:
        return

    for num in range(start, H*(N-1)):
        i = num//(N-1)
        j = num%(N-1)
        if not G[i][j] and check_available(i, j):
            G[i][j] = True
            dfs(start + 1 if start%(N-1) == N-2 else start + 2, cnt + 1)
            G[i][j] = False

# main
N, M, H = map(int, input().split())
G = [[False]*N for _ in range(H)] # 0~N-2, 0~H-1
for _ in range(M):
    a, b = map(int ,input().split())
    G[a-1][b-1] = True

ans = 4
dfs(0, 0)
print(ans if ans<=3 else -1)