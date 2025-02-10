# https://www.acmicpc.net/problem/15649

def back_track(depth):
    if depth == M:
        print(' '.join(map(str, output)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            output.append(i+1)
            back_track(depth+1)
            visited[i] = False
            output.pop()


N, M = map(int, input().split())
# 중복 순열 방지
visited = [False] * N
output = []

back_track(0)