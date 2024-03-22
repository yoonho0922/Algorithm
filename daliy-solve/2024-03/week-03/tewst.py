import sys
sys.setrecursionlimit(3000)

# 사전순은 d l r u
direct = ['d', 'l', 'r', 'u']
dx = [1,0,0,-1]
dy = [0,-1,1,0]


def dfs(n, m, k, x,y, r,c, S):
    # print('k, x,y, r,c, S',k, x,y, r,c, S)

    if k == 0:
        return S

    short = get_shortest(x,y, r,c)

    if short > k or (k - short)%2==1:
        return ''

    for i in range(4):
        d = direct[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if not (1<=nx<=n and 1<=ny<=m):
            continue

        route = dfs(n, m, k-1, nx,ny, r,c, S + d)

        if route != '':
            return route




def get_shortest(x,y,r,c):
    return abs(x-r) + abs(y-c)

def solution(n, m, x, y, r, c, k):
    short = get_shortest(x,y, r,c)

    route = dfs(n, m, k, x,y, r,c, '')

    return route if route != '' else "impossible"