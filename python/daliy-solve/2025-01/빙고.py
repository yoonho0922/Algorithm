# https://www.acmicpc.net/problem/2578

def bingo(board):
    cnt = 0
    # 1. 가로 체크
    for r in range(5):
        if all(board[r]):
            cnt += 1

    # 2. 세로 체크
    for c in range(5):
        if all(list(zip(*board))[c]):
            cnt += 1

    # 3. 대각선 체크
    rightUppers = []
    leftUppers = []
    for i in range(5):
        rightUppers.append(board[4-i][i])
        leftUppers.append(board[i][i])
    if all(rightUppers):
        cnt += 1
    if all(leftUppers):
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False

def solution(board, positions, calls):
    cnt = 0

    for calls_row in calls:
        for call in calls_row:
            cnt += 1
            r, c = positions[call] # (y,x)
            board[r][c] = True

            if bingo(board):
                return cnt

    raise Exception("잘못된 입력")

board = [[False] * 5 for _ in range(5)]
positions = dict() # (번호, (y, x))

for r in range(5):
    nums = list(map(int, input().split()))
    for c in range(5):
        positions[nums[c]] = (r, c)

calls = [list(map(int, input().split())) for _ in range(5)]

answer = solution(board, positions, calls)

print(answer)