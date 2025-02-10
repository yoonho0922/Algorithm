# https://www.acmicpc.net/problem/9372

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        _ = input().split()
    print(N-1)