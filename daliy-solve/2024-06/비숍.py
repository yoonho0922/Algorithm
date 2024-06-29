# https://www.acmicpc.net/problem/1799

def dfs(right_up, cnt):
    global ans

    if  right_up == TOTAL_DIALOG:
        ans = max(cnt, ans)
        return
    # dfs 를 더 탐색 했을 때 얻을 수 있는 최대 값 (실제론 visited_right_down 을 고려하기 때문에 더 적은 값이 나올 수 있음)
    if (TOTAL_DIALOG - right_up) + cnt <= ans:
        return

    # 정해진 right_up 에서 x, y에 말을 두는 경우
    for y in range(N):
        x = right_up - y
        right_down = N - 1 + (y-x)
        if 0<=x<N and 0<=y<N and G[y][x] == 1 and not visited_right_down[right_down]:
            visited_right_down[right_down] = True
            dfs(right_up+1, cnt+1)
            visited_right_down[right_down] = False

    # 정해진 right_up 에서 x, y에 말을 두지 않는 경우
    dfs(right_up+1, cnt)

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

TOTAL_DIALOG = N*2-1

visited_right_down = [False] * TOTAL_DIALOG
ans = 0

dfs(0, 0)

print(ans)