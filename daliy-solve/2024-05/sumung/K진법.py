import sys
readline = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    ans = [0] * K
    s = str(N)
    size = len(s)

    # 나온 숫자
    for i in range(K):
        total = 0

        # 자릿수
        for j in range(1, size+1):
            # 1의자리
            total += (N // (K**j)) * (K**(j-1))

            if i!=0 and int(s[-j]) >= i:
                total += (K**(j-1))

        ans[i] += total

    print(' '.join(map(str,ans)))