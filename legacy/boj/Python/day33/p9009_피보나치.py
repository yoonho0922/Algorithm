import sys
readline = sys.stdin.readline

d = [0,1] + [0] * 48

for i in range(2, len(d)):
    d[i] = d[i-1] + d[i-2]

T = int(readline())
for _ in range(T):
    N = int(readline())
    ans = []

    for i in range(len(d)-1, -1, -1):
        if d[i] <= N:
            ans.append(d[i])
            N -= d[i]
        if N == 0:
            break

    ans.sort()
    for a in ans:
        print(a, end=' ')
    print()