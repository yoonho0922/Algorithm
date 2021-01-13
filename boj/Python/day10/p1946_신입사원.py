import sys
readline = sys.stdin.readline

T = int(readline())

for _ in range(T):

    N = int(readline())
    scores = [0] * (N + 1)

    for _ in range(N):
        l = list(map(int, readline().split()))
        scores[l[0]] = l[1]

    cnt = 1
    low = scores[1]

    for i in range(2, N+1):
        # 면접 성적 순위가 더 높으면
        if scores[i] < low:
            cnt += 1
            low = scores[i]

    print(cnt)