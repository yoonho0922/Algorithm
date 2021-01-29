import sys
readline = sys.stdin.readline

def install(distance):
    count = 1
    cur = homes[0]

    for home in homes:
        if home - cur >= distance:
            count += 1
            cur = home
    return count

N, C = map(int, readline().split())
homes = []
for _ in range(N):
    homes.append(int(readline()))

homes.sort()
left, right, ans = 1, homes[-1] - homes[0], 0

while left <= right:
    mid = (left + right) // 2

    if install(mid) >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)