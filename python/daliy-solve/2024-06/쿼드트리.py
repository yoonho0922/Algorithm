# https://www.acmicpc.net/problem/1992

def check_binary(size, cy, cx):
    for i in range(cy, cy+size):
        for j in range(cx, cx+size):
            if G[i][j] != G[cy][cx]:
                return -1
    return G[cy][cx]


def compress(size, cy, cx):
    ans = ''
    binary = check_binary(size, cy, cx)

    if binary == -1:
        ans += '('
        for i in range(cy, cy+size, size//2):
            for j in range(cx, cx+size, size//2):
                ans += compress(size//2, i, j)
        ans += ')'
    else:
        ans += binary
    return ans




N = int(input())
G = [input() for _ in range(N)]

print(compress(N, 0, 0))