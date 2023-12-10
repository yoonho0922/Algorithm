def exp(x):
    total = 0
    for i in range(6):
        for j in range(6):
            total += sum(d[x][i][j])
    return total/216

def prize(i,j,k):
    if i == j == k:
        return 10000 + (k + 1) * 1000
    elif i == j:
        return 1000 + (j + 1) * 100
    elif i == k:
        return 1000 + (k + 1) * 100
    elif j == k:
        return 1000 + (k + 1) * 100
    else:
        return (max([i, j, k]) + 1) * 100

def sol(x):
    # 기회가  x 번 남았을 때, 주사위 눈이 순서대로 i, j, k 가 나왔을 경우
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if x == 0:
                    d[x][i][j][k] = prize(i, j, k)
                else:
                    # i, j, k가 나오고 한 번 더 수행했을 때 얻을 수 있는 기댓값
                    # j, k, (1~6) 의 상금 / 6
                    e = sum(d[x - 1][j][k]) / 6

                    # 현재 상태가 한 번 더 수행했을 때 기댓값보다 높으면 멈춤
                    # 그전 점수를 그대로 가져옴
                    if d[x - 1][i][j][k] > e:
                        d[x][i][j][k] = d[x - 1][i][j][k]
                    # 기댓값이 높으면 한 번 더 수행한다고 생각
                    # 해당 기댓값을 저장
                    else:
                        d[x][i][j][k] = e


N = int(input())
d = [[[[0.0]*6 for _ in range(6)] for _ in range(6)] for _ in range(N)]
E = [0.0]*N

# 기회가 x 번 남았을 때 확률 구하기
for x in range(N-2):
    sol(x)
    E[x + 1] = exp(x)

print(E[N-2])