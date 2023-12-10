S = 9 # SIZE

def get_candi(y, x):
    candi = [i+1 for i in range(9)]

    # 가로 세로 검사
    for i in range(S):
        if matrix[y][i] in candi:
            candi.remove(matrix[y][i])
        if matrix[i][x] in candi:
            candi.remove(matrix[i][x])
    # 3*3 검사
    b, a = y//3, x//3
    for i in range(3):
        for j in range(3):
            if matrix[b*3+i][a*3+j] in candi:
                candi.remove(matrix[b*3+i][a*3+j])

    return candi

def sol(cnt):
    if cnt == len(blanks):
        for row in matrix:
            print(*row)
        exit()

    (y, x) = blanks[cnt]
    candi = get_candi(y, x)

    for c in candi:
        matrix[y][x] = c
        sol(cnt+1)
        matrix[y][x] = 0



# input
matrix = [list(map(int, input().split())) for _ in range(S)]
blanks = [(i,j) for i in range(S) for j in range(S) if matrix[i][j]==0]

sol(0)