# https://www.acmicpc.net/problem/2559

N, K = map(int, input().split())
A = list(map(int, input().split()))

sums = [A[0]]

for i in range(1, N):
    sums.append(sums[i-1] + A[i])

ans = sums[K-1]

for i in range(K, N):
    ans = max(ans, sums[i] - sums[i-K])

print(ans)