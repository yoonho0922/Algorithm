def sol(depth, x):
    if depth == M:
        print(' '.join(map(str, out)))
        return

    for i in range(x, N):
        if not visited[i]:
            out.append(i+1)
            sol(depth+1, i)
            out.pop()


N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

sol(0,0)