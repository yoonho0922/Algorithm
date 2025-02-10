# https://www.acmicpc.net/problem/8979

N, K = map(int, input().split())

countries = []
target = []

for _ in range(N):
    n, g, s, b = map(int, input().split())
    countries.append([g, s, b])
    if n == K:
        target = [g, s, b]

ans = 0

for g, s, b in countries:
    if g > target[0]:
        ans += 1
    elif g == target[0] and s > target[1]:
        ans += 1
    elif g == target[0] and s == target[1] and b > target[2]:
        ans += 1

print(ans+1)
