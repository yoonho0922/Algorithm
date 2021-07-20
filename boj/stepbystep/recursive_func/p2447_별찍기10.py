def sol(num, a, b):
    if num==1:
        matrix[a][b]='*'
        return

    for i in range(a, a+num, num//3):
        for j in range(b, b+num, num//3):

            if i==a+num//3 and j==b+num//3:
                continue
            sol(num//3, i, j)

N = int(input())
matrix = [[' ']*N for _ in range(N)]

sol(N,0,0)

for row in matrix:
    # print(row)
    print(''.join(map(str, row)))