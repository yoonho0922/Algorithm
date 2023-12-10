import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
white, black = [], []
for i in range(N):
    line = list(readline().strip())

    # 맨 왼쪽 위가 블랙
    bLine = []
    if i%2 == 0:
        for j in range(M):
            if j%2 == 0 and line[j] != 'B':
                bLine.append(1)
            elif j%2 == 1 and line[j] != 'W':
                bLine.append(1)
            else:
                bLine.append(0)
    else:
        for j in range(M):
            if j%2 == 0 and line[j] != 'W':
                bLine.append(1)
            elif j%2 == 1 and line[j] != 'B':
                bLine.append(1)
            else:
                bLine.append(0)
    black.append(bLine)

    # 맨 왼쪽 위가 화이트
    wLine = []
    if i % 2 == 0:
        for j in range(M):
            if j % 2 == 0 and line[j] != 'W':
                wLine.append(1)
            elif j % 2 == 1 and line[j] != 'B':
                wLine.append(1)
            else:
                wLine.append(0)
    else:
        for j in range(M):
            if j % 2 == 0 and line[j] != 'B':
                wLine.append(1)
            elif j % 2 == 1 and line[j] != 'W':
                wLine.append(1)
            else:
                wLine.append(0)
    white.append(wLine)

ans = 1000000000
for i in range(N-7):
    for j in range(M-7):
        count = [0, 0]
        for k in range(i, i+8):
            count[0] += sum(white[k][j:j+8])
            count[1] += sum(black[k][j:j+8])
        ans = min(ans, count[0], count[1])
print(ans)