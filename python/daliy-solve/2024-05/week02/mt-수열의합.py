# https://www.acmicpc.net/problem/1024

MAX_LENGTH = 100

def get_list(N, L):
    for d in range(L, MAX_LENGTH + 1):
        if 2*N % d == 0 and ((2*N//d) - d + 1) % 2 == 0:
            a = ((2*N//d) - d + 1) // 2
            if a>=0:
                return [i for i in range(a,a+d)]

    return []


N, L = map(int, input().split())

result = get_list(N, L)

if result:
    print(*result)
else:
    print(-1)