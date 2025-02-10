# https://www.acmicpc.net/problem/21921

N, X = map(int, input().split())
visitors = list(map(int, input().split()))


now_visitors = sum(visitors[:X])
max_visitors = now_visitors
cnt = 1

l, r = 1, X
while r < N:
    now_visitors += visitors[r]
    now_visitors -= visitors[l-1]
    if now_visitors == max_visitors:
        cnt += 1
    elif now_visitors > max_visitors:
        max_visitors = now_visitors
        cnt = 1
    l += 1
    r += 1

if max_visitors != 0:
    print(max_visitors)
    print(cnt)
else:
    print("SAD")