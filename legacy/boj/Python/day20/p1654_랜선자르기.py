import sys
readline = sys.stdin.readline

K, N = map(int, readline().split())
lans = []
for _ in range(K):
    lans.append(int(readline()))

left, right, ans = 1, max(lans), 0

while left <= right:
    mid = (left+right)//2
    sum_lan = 0

    for i in lans:
        sum_lan += i // mid

    if sum_lan >= N:
        ans = mid
        left = mid + 1
    elif sum_lan < N:
        right = mid - 1

print(ans)