# https://www.acmicpc.net/problem/13460

from collections import defaultdict
from collections import deque

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

def bfs(r, b):
    q = deque()

    q.append([r[0],r[1],b[0],b[1]])
    visited[R[0],R[1],B[0],B[1]] = True

    cnt = 0

    while q:
        if cnt > 10:
            return -1

        for _ in range(len(q)):
            rcy, rcx, bcy, bcx = q.popleft()

            # 파랑이 빠져나오면 무시
            if G[bcy][bcx] == 'O':
                continue

            # 파랑이 안빠져나오고 빨간구슬이 나왔다면 성공
            if [rcy, rcx] == goal:
                return cnt

            # 상하좌우 기울기 동 서 남 북
            for i in range(4):
                # 기울이고 이동
                nr = tilt(rcy, rcx, i, bcy, bcx)
                nb = tilt(bcy, bcx, i, rcy, rcx)

                # 탐색한 루트가 아니라면 조사
                if not visited[(nr[0], nr[1], nb[0], nb[1])]:
                    visited[(nr[0], nr[1], nb[0], nb[1])] = True
                    q.append([nr[0], nr[1], nb[0], nb[1]])

        cnt += 1

    return -1

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

print(bfs(R, B))