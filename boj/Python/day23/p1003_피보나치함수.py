import sys
readline = sys.stdin.readline

d = [[0]*2 for _ in range(41)]
d[0][0], d[1][1] = 1, 1

for x in range(2, 41):
    # 0의 갯수 구하기
    d[x][0] = d[x - 1][0] + d[x - 2][0]
    # 1의 갯수 구하기
    d[x][1] = d[x - 1][1] + d[x - 2][1]

T = int(readline())


for _ in range(T):

    N = int(readline())
    print(d[N][0], d[N][1])