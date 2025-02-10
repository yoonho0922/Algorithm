# https://www.acmicpc.net/problem/17140

A_LENGTH = 3
MAX_LENGTH = 100
MAX_TIME = 100


def sort_row(n, m, G):
    # 1. 행에 대해서 정렬을 수행한다
    # 2. 늘어난 m을 반환한다
    max_m = m

    for r in range(n):
        number_cnt = {}
        for c in range(m):
            if G[r][c]:
                number = G[r][c]
                if number_cnt.get(number):
                    number_cnt[number] += 1
                else:
                    number_cnt[number] = 1

        col = 0
        sorted_number_cnt = sorted(number_cnt.items(), key= lambda x:[x[1],x[0]])
        for number, cnt in sorted_number_cnt:
            G[r][col] = number
            G[r][col+1] = cnt
            col += 2
        for c in range(col, m):
            G[r][c] = 0
        max_m = max(max_m, col)

    return max_m


R, C, K = map(int, input().split())
G = [[0]*MAX_LENGTH for _ in range(MAX_LENGTH)]

for i  in range(A_LENGTH):
    row = list(map(int, input().split()))
    for j in range(A_LENGTH):
        G[i][j] = row[j]

n, m = 3, 3

for step in range(MAX_TIME + 1):
    if G[R-1][C-1] == K:
        print(step)
        break

    if n >= m:
        # 모든 행에 대해서 정렬을 수행한다
        updated_m = sort_row(n, m, G)

        # 배열 크기 업데이트
        m = updated_m
    else:
        # 행열 뒤집기
        n, m = m, n
        G = [list(r) for r in zip(*G)]

        # 모든 행에 대해서 정렬을 수행한다
        updated_m = sort_row(n, m, G)

        # 배열 크기 업데이트
        m = updated_m

        # 행열 뒤집기
        n, m = m, n
        G = [list(r) for r in zip(*G)]

else:
    print(-1)


