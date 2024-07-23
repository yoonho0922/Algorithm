# https://www.acmicpc.net/problem/6064

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = -1

    y = y if y<N else 0
    for i in range(N):
        k = M*i + x
        if k % N == y:
            ans = k
            break

    print(ans)
