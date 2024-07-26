# https://www.acmicpc.net/problem/1748

A = input()
N = len(A)

ans = 0

for i in range(1, N):
    ans += i * 9 * 10**(i-1)

ans += (int(A) - 10**(N-1) + 1) * N

print(ans)