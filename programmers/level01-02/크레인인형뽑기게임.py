def solution(board, moves):
    answer = 0
    N = len(board[0])
    height = [0] * N
    pocket = [-1]

    for i in range(len(board[0])):
        while board[height[i]][i] == 0 and height[i] < N:
            height[i] += 1

    for i in moves:
        if height[i-1] == N:
            continue

        item = board[height[i-1]][i-1]
        board[height[i-1]][i-1] = 0

        if pocket[-1] == item:
            pocket.pop()
            answer += 2
        else:
            pocket.append(item)
        height[i-1] += 1

    return answer