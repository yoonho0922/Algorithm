# https://www.acmicpc.net/problem/14891


def rotate(wheel, d):
    if d == 1:
        # 시계 회전
        tmp = wheel[7]
        for i in range(7, 0, -1):
            wheel[i] = wheel[i-1]
        wheel[0] = tmp
    else:
        # 반시계 회전
        tmp = wheel[0]
        for i in range(0, 7):
            wheel[i] = wheel[i+1]
        wheel[7] = tmp

def get_rotates(wheels, origin, direct):
    result = [[origin,direct]]

    # left cur=origin~1
    for cur in range(origin,0,-1):
        next = cur-1
        if wheels[cur][6] != wheels[next][2]:
            result.append([next, direct * int((-1)**(origin-next))])
        else:
            break
    # right cur=origin~2
    for cur in range(origin,3):
        next = cur+1
        if wheels[cur][2] != wheels[next][6]:
            result.append([next, direct * int((-1)**(origin-next))])
        else:
            break

    return result

# 입력 받기
wheels = [list(map(int, input())) for _ in range(4)]
K = int(input())

for _ in range(K):
    num, direct = map(int, input().split()) # 1: 시계, -1: 반시계

    # [[number, direct]]
    rotates = get_rotates(wheels, num-1, direct)

    for target, d in rotates:
        rotate(wheels[target], d)

ans = 0

for i in range(4):
    if wheels[i][0]==1:
        ans += 2 ** i

print(ans)