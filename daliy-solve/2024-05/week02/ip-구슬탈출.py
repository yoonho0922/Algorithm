# https://www.acmicpc.net/problem/13460

from collections import defaultdict

dy = [0,0,1,-1]
dx = [1,-1,0,0]


def tilt(cy, cx, direct, antY, antX):
    isHole = False
    isAnother = False
    toMove = [cy, cx]

    for dist in range(1, max(N,M)-2):
        ny = cy + dy[direct] * dist
        nx = cx + dx[direct] * dist

        if 0<ny<N-1 and 0<nx<M-1:
            if  G[ny][nx] == '#':
                break

            # 이동할 수 있다면
            toMove[0] = ny
            toMove[1] = nx

            if G[ny][nx] == 'O':
                isHole = True
                break
            if [ny, nx] == [antY, antX]:
                isAnother = True

        else:
            break


    # 구멍이 있으면 다른 구슬과 상관없이 구멍으로 이동
    if isHole:
        return toMove
    # 구멍이 없고, 다른 구술이 움직이는 방향에 있다면, 끝 지점의 직전으로 이동
    if isAnother:
        return [toMove[0] - dy[direct], toMove[1] - dx[direct]]
    # 구멍이 없고 다른 구슬도 없다면, 끝 지점으로 이동
    return toMove


def dfs(r, b, depth):
    global ans

    # 가지치기
    if depth > 10:
        return

    # 성공했다면
    if r == goal:
        ans = depth if ans==-1 else min(ans, depth)
        print('success!', depth, r, goal, '\n')
        return

    # 상하좌우 기울기 동 서 남 북
    for i in range(4):
        # 기울이고 이동
        nr = tilt(r[0], r[1], i, b[0], b[1])
        nb = tilt(b[0], b[1], i, r[0], r[1])


        # 파랑이 빠져나오면 실패
        if G[nb[0]][nb[1]] == 'O':
            return

        # 탐색한 루트가 아니라면 조사
        if not visited[(nr[0], nr[1], nb[0], nb[1])]:

            print('nr, nb', '-'*depth, i, nr, nb)
            print()

            visited[(nr[0], nr[1], nb[0], nb[1])] = True
            dfs(nr, nb, depth + 1)


N, M = map(int,input().split())
G = []
R, B, goal = [], [], [] # R, B, O의 위치 [y, x]

for i in range(N):
    row = list(input())
    if 'R' in row:
        R = [i, row.index('R')]
    if 'B' in row:
        B = [i, row.index('B')]
    if 'O' in row:
        goal = [i, row.index('O')]
    G.append(row)

visited = defaultdict(bool) # (ry,rx,by,bx) 방문 여부
visited[R[0],R[1],B[0],B[1]] = True

ans = -1

dfs(R, B, 0)

print(ans)


# logging
for i in range(N):
    print(G[i])
print(R, B, goal)
