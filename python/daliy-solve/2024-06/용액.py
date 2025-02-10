# https://www.acmicpc.net/problem/2467

N = int(input())
S = list(map(int, input().split()))

l, r, now = 0, N-1, (S[0] + S[N-1])
ans, al, ar = now, l, r

while l<r:
    tmp = S[l] + S[r]

    if abs(tmp) < abs(ans):
        ans = tmp
        al, ar = l, r

    if tmp == 0:
        break
    elif tmp < 0:
        l += 1
    else:
        r -= 1

print(S[al], S[ar])