# 상하좌우

n = int(input())
plans = input().split()
# print(plans)
cy, cx = 1, 1

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
arrow = ['U','D','R','L']

for plan in plans:
    for i in range(len(arrow)):
        if plan == arrow[i]:
            # print(arrow[i])
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not (nx > n or ny > n or nx < 1 or ny <1):
                cx = nx
                cy = ny

            # print(cx, cy)
            break

print(cx, cy)