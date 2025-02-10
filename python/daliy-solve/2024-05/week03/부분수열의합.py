# https://www.acmicpc.net/problem/1182

def back_track(partial, start):
    global ans

    if len(partial) >0 and sum(partial) == S:
        ans += 1

    for i in range(start, N):
        back_track(partial + [numbers[i]], i+1)


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

visited = [False] * N
ans = 0

back_track([], 0)

print(ans)