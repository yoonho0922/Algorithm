# 게임개발

M, N = map(int, input().split())
cy, cx, d = map(int, input().split())
array = []
check = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    array.append(list(map(int, input().split())))

dy = [1,0,-1,0] # 북 동 남 서
dx = [0,1,0,-1]

count = 0
for _ in range (10):
    # print(cy, cx)
    for i in range(4):
        nd = (d+3+i)%4
        ny=cy+dy[nd]
        nx=cx+dx[nd]
        if (0<=ny<N and 0<=nx<M) and (array[ny][nx] == 0 and not check[ny][nx]):
            cy, cx = ny, nx
            count += 1
            d = nd
            check[ny][nx]=True
            # print('break')
            break
    else:
        # print('back')
        nd = (d+2)%4
        ny=cy+dy[nd]
        nx=cx+dx[nd]
        if (0<=ny<N and 0<=nx<M) and (array[ny][nx] == 0):
            cy, cx = ny, nx
        else:
            break

    # print(check)

print(count)