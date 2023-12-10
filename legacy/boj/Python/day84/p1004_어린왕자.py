import sys
readline = sys.stdin.readline

# 지나야 하는 원의 수를 구하는 함수
def countCircle():
    cnt = 0
    for cx, cy, r in circles:
        sdist = pow(sx-cx, 2) + pow(sy-cy, 2)
        edist = pow(ex-cx, 2) + pow(ey-cy, 2)

        if sdist < pow(r, 2) and edist > pow(r, 2):
            # 시작점에서 거쳐야하는 원
            cnt += 1
        elif sdist > pow(r, 2) and edist < pow(r, 2):
            # 도착점에서 거쳐야하는 원
            cnt += 1

    return cnt

T = int(readline())
for _ in range(T):
    sx, sy, ex, ey = map(int, readline().split())
    N = int(readline())
    circles = []
    for _ in range(N):
        circles.append(list(map(int, readline().split())))

    ans = 0
    ans += countCircle()

    print(ans)