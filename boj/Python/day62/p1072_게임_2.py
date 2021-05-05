import sys
readline = sys.stdin.readline

X, Y = map(int, readline().split())

rate = Y*100//X
left, right, ans = 0, X, -1

while left <= right:
    mid = (left + right) // 2

    cur_rate = (Y+mid)*100//(X+mid)

    if cur_rate > rate:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)