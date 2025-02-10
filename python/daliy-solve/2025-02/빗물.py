# https://www.acmicpc.net/problem/14719

def check_disable_side(y, x):
    if G[y][x] == 'O':
        G[y][x] = 'X'
        if x-1 >= 0:
            check_disable_side(y, x - 1)
        if x+1 < W:
            check_disable_side(y, x + 1)
    else:
        return


# 입력
H, W = map(int, input().split())
# 뒤집혀 있음 주의
# O : 빈공간, R : 빗물, B : 블록, X : 고일 수 없는 공간
G = [['O'] * W for _ in range(H)]
max_height = 0
for x, y in enumerate(list(map(int, input().split()))):
    max_height = max(max_height, y)
    for i in range(y):
        G[i][x] = 'B'

answer = 0
# 한칸씩 높이기
for y in range(max_height):
    # 양옆 불가능한거 체크
    check_disable_side(y, 0)
    check_disable_side(y, W - 1)
    # 빗물 고일 수 있는 거 체크
    for x in range(W):
        if G[y][x] == 'O':
            answer += 1

print(answer)