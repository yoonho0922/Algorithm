# https://www.acmicpc.net/problem/19939

N, K = map(int, input().split())
min_n = sum(range(1,K+1))

if N < min_n:
    print(-1)
else:
    if (N-min_n)%K==0:
        print(K-1)
    else:
        print(K)
