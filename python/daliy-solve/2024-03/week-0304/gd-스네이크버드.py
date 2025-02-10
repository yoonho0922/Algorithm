# https://www.acmicpc.net/problem/16435


N, size = map(int, input().split())
H = list(map(int, input().split()))

for height in sorted(H):
    if height <= size:
        size += 1
    else:
        break

print(size)