# https://www.acmicpc.net/problem/12100

# 1. 방향을 받아서 블록을 합치는 함수
# 2. dfs 진행하며 최대 5번 이동하고 존재하는 블록의 최대값 - 이동할 수 없다면 back

# 블록 이동하기
# 북쪽이동: 열 순서대로 이동하며(i) 행순서대로 검사(j) j+1부터 N-1까지 검사하는 k
# if G[j][i] != 0: if 둘이 같으면 G[j][i] == G[k][i]일때 합치기 아니면 G[k][i] -> G[j+1][i] 이동하기,
# floor: 이동할 수 있는 최상단
# if G[j][i] == 0: floor=0 G[k][i]에 블록이 있다면 floor로 옮기고 G[j][i]를 대상으로 다시 합치기 로직
# if G[j][i] != 0: floor = j

# 북, 서, 남, 동: 0도, 90도, 180도, 270도 회전하여 북쪽이동 로직

def get_max(G):
    result = 0
    for i in range(len(G)):
        for j in range(len(G)):
            result = max(result, G[i][j])
    return result


def move(G, N):
    moved = False

    for i in range(N):
        for j in range(N-1):
            if G[j][i] == 0:
                for k in range(j+1, N):
                    if G[k][i] != 0:
                        # 숫자 블록을 0이 있던 곳으로 이동
                        G[j][i], G[k][i] = G[k][i], 0
                        moved = True
                        break

            if G[j][i] != 0:
                for k in range(j+1, N):
                    if G[k][i] == 0:
                        continue

                    # 같은 숫자가 있다면 블록 합치기
                    if G[k][i] == G[j][i]:
                        G[j][i], G[k][i] = G[j][i] * 2, 0
                        moved = True
                        break

                    # 다른 숫자가 있다면
                    else:
                        # 바로 아래의 다른 숫자라면 옮길 수 없음
                        if k == j+1:
                            break

                        # 한칸 떨어져 있다면 옮기기
                        G[j+1][i], G[k][i] = G[k][i], 0
                        moved = True
                        break

    return moved, G


def dfs(G, N, depth, movable):
    global ans

    # print('depth', depth, movable)
    # for i in range(N): print(G[i])

    # 움직일 수 없거나 5번 움직였다면 종료
    # debug
    if not movable or depth == 5:
        max_num = get_max(G)
        ans = max(ans, max_num)
        return

    for direct in ['N','W','S','E']:
        # print('direct', direct)

        # 북쪽
        if direct == 'N':
            moved, moved_G = move([list(x[:]) for x in G], N)
            reverted = moved_G
            dfs(reverted, N, depth + 1, moved)
        # 서쪽
        elif direct == 'W':
            # 90도 회전: x, -y
            # print('origin')
            # for i in range(N): print(G[i])
            rotated = [list(x[:]) for x in zip(*G[::-1])]
            # print('direct', direct)
            # for i in range(N): print(rotated[i])
            moved, moved_G = move(rotated, N)
            # -90도 회전: -x, y
            reverted = [list(x[:]) for x in zip(*moved_G)][::-1]
            dfs(reverted, N, depth + 1, moved)
        # 남쪽
        elif direct == 'S':
            # 180도 회전
            # print('origin')
            # for i in range(N): print(G[i])
            rotated = [list(x[::-1]) for x in G[::-1]]
            # print('direct', direct)
            # for i in range(N): print(rotated[i])
            moved, moved_G = move(rotated, N)
            # -180도 회전
            rotated = [list(x[::-1]) for x in moved_G[::-1]]
            dfs(rotated, N, depth + 1, moved)
        # 동쪽
        else:
            # -90도 회전: x, -y
            # print('origin')
            # for i in range(N): print(G[i])
            rotated = [list(x[:]) for x in zip(*G)][::-1]
            # print('direct', direct)
            # for i in range(N): print(rotated[i])
            moved, moved_G = move(rotated, N)
            # 90도 회전: -x, y
            reverted = [list(x[:]) for x in zip(*moved_G[::-1])]
            dfs(reverted, N, depth + 1, moved)

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

ans = 0

dfs(G, N, 0, True)

print(ans)