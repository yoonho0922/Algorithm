# https://www.acmicpc.net/problem/2346

def move(idx, b, removed):
    cnt = 0
    if b > 0:
        while cnt != b:
            idx = idx + 1 if idx + 1 < N else 0
            if not removed[idx]:
                cnt += 1
    else:
        while cnt != abs(b):
            idx = idx - 1 if idx > 0 else N - 1
            if not removed[idx]:
                cnt += 1
    return idx

N = int(input())
balloons = list(map(int,input().split()))
removed = [False] * N

idx = 0
ans = [idx+1]
removed[idx] = True

for _ in range(N-1):
    idx = move(idx, balloons[idx], removed)
    ans.append(idx+1)
    removed[idx] = True

print(*ans)