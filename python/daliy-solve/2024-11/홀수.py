# https://www.acmicpc.net/problem/2576

N = 7
odds = []
for _ in range(N):
    num = int(input())
    if num % 2 == 1:
        odds.append(num)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)