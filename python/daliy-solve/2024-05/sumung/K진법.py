# 실패

import sys
readline = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    ans = [0] * K
    s = str(N)
    size = len(s)

    # 나온 숫자
    for i in range(1, K):
        total = 0

        # 자릿수
        for j in range(1, size+1):
            if i != 0:
                total += (N // (K**j)) * (K**(j-1))
            else:
                total += (N // (K**j)) * (K**(j-1)-1)

                if j != 1:
                    total += int(s[(-j+1)]) + 1
                else:
                    total += int(s[-1])


            if i!=0 and int(s[-j]) > i:
                total += (K**(j-1))
            elif i!=0 and int(s[-j]) == i:
                if j==1:
                    total += 1
                else:
                    # print(size, i, j, s[-j+1:])
                    total += int(s[-j+1:]) + 1




        ans[i] += total

    total = 0

    # 자릿수
    for j in range(1, size+1):
        total += (N // (K**j)) * (K**(j-1)-1)

        # ....

    ans[0] += total

    print(' '.join(map(str,ans)))