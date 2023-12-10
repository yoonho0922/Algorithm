import sys
readline = sys.stdin.readline

N, C = map(int, readline().split())
homes = []
for _ in range(N):
    homes.append(int(readline()))
homes.sort()

def inspect(dist):
    pre, count = homes[0], 1
    for i in range(1, N):
        if homes[i] - pre >= dist:
            count += 1
            pre = homes[i]
    return count >= C

left, right, ans = 0, homes[-1], 0
while left <= right:
    mid = (left + right) // 2

    if inspect(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)