# https://www.acmicpc.net/problem/1940

N = int(input())
M = int(input())
S = list(map(int, input().split()))

S.sort()

total, r, l = 0, 0, N-1

while r < l:
    res = S[r] + S[l]

    if res == M:
        total += 1
        r += 1
        l -= 1
    elif res < M:
        r += 1
    else:
        l -= 1
print(total)