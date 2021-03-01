import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
coins = []
for _ in range(N):
    coins.append(int(readline()))
ans = 0

for i in range(N-1, -1, -1):
    if K == 0:
        break
    ans += K // coins[i]
    K = K % coins[i]
print(ans)
