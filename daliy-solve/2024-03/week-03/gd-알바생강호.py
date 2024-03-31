# https://www.acmicpc.net/problem/1758

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort(reverse=True)
ans = 0

for i in range(N):
    ans += max(A[i] - i, 0)

print(ans)