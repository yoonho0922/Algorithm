def sol(depth):
    if depth == M:
        print(' '.join(map(str, out)))

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            out.append(i+1)
            sol(depth+1)
            visited[i]=False
            out.pop()


N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

sol(0)