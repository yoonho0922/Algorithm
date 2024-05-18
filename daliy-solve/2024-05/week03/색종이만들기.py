# https://www.acmicpc.net/problem/2630

def get_color(sy, sx, size):
    w, b = 0, 0
    for i in range(sy, sy+size):
        for j in range(sx, sx+size):
            if G[i][j] == 0:
                w +=1
            else:
                b += 1

    # print('size, w,b', size, w, b)

    if b == 0:
        return 0
    elif w == 0:
        return 1
    else:
        return -1


def cut(sy, sx, degree):
    w, b = 0, 0
    size = int(N/pow(2,degree))
    part_size = int(N/pow(2,degree+1))

    for i in range(sy, sy+size, part_size):
        for j in range(sx, sx+size, part_size):
            color = get_color(i, j, part_size)

            if color == 0:
                # white
                w += 1
            elif color == 1:
                b += 1
            else:
                # 혼합 색일 경우
                split_w, split_b = cut(i, j, degree+1)
                w += split_w
                b += split_b

    return w, b


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

degree = 0

color = get_color(0, 0, N)

if color == -1:
    w, b = cut(0, 0, 0)
    print(w)
    print(b)
elif color ==0:
    print(1)
    print(0)
else:
    print(0)
    print(1)
