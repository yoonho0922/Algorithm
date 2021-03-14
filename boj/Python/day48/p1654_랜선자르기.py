import sys
readline = sys.stdin.readline

K, N = map(int, readline().split())
wires = []
for _ in range(K):
    wires.append(int(readline()))

ans, left, right = 0, 1, max(wires)
while left <= right:
    mid = (left + right) // 2
    count = 0
    for wire in wires:
        count += wire // mid
    if count >= N:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)