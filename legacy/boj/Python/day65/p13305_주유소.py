import sys
readline = sys.stdin.readline

N = int(readline())
loads = list(map(int, readline().split()))
prices = list(map(int, readline().split()))

ans = 0
cur, next, dist = prices[0], 0, 0

for i in range(1, N-1):
    if prices[i] < cur:
        ans += cur * (dist + loads[i-1])
        cur = prices[i]
        dist = 0
    else:
        dist += loads[i-1]

ans += cur * (dist + loads[N-2])

print(ans)