import sys
readline = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    ans = [0] * K

    for i in range(1, N+1):
        s = str(i)

        for num in s:
            ans[int(num)] += 1


    print(' '.join(map(str,ans)))