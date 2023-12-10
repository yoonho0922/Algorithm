import sys
readline = sys.stdin.readline

N = int(readline())
ropes = []
for _ in range(N):
    ropes.append(int(readline()))
ropes.sort(reverse=True)
ans = 0
for i in range(N):
    if ropes[i] * (i+1) > ans:
        ans = ropes[i] * (i+1)
print(ans)