from sys import stdin

N = int(stdin.readline())

ropes = []
for _ in range(N):
    ropes.append(int(stdin.readline()))

ropes.sort(reverse=True)

max_w = ropes[0]

for k in range(2, N+1):
    w = ropes[k-1] * k # 선택한 로프 중 가장 약한 로프

    if max_w < w:
        max_w = w

print(max_w)