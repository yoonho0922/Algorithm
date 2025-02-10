# https://www.acmicpc.net/problem/10431

def sorting(S):
    cnt = 0
    for i in range(1, len(S)):
        for j in range(i, 0, -1):
            if S[j] < S[j-1]:
                S[j], S[j-1] = S[j-1], S[j]
                cnt += 1

    return cnt

T = int(input())
for _ in range(T):
    s = list(map(int, input().split()))
    print(s[0], sorting(s[1:]))
