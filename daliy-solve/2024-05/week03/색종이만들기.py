# https://www.acmicpc.net/problem/2630

def is_mixed(sy, sx, size):
    w, b = 0, 0
    for i in range(sy, sy+size):
        for j in range(sx, sx+size):
            if G[i][j] == 0:
                w += 1
            else:
                b += 1

    return w>0 and b>0


def get_color(sy, sx, size):
    if not is_mixed(sy, sx, size):
        if G[sy][sx] == 0:
            return [1, 0]
        else:
            return [0, 1]

    w, b = 0, 0

    for i in range(sy, sy+size, int(size/2)):
        for j in range(sx, sx+size, int(size/2)):
            split_w, split_b = get_color(i, j, int(size/2))
            w += split_w
            b += split_b

    return [w, b]


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

degree = 0

color = get_color(0, 0, N)
print('\n'.join(map(str,color)))