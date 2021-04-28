import sys
readline = sys.stdin.readline

N = int(readline())
S = []
for _ in range(N):
    S.append(list(map(int, readline().split())))
S.sort(key=lambda x: (x[1], x[0]))
ans = 0
prior = 0

for s in S:
    if s[0] >= prior:
        ans += 1
        prior = s[1]
print(ans)