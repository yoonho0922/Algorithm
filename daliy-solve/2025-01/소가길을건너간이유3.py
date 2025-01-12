# https://www.acmicpc.net/problem/14469

N = int(input())
cows = [list(map(int,input().split())) for _ in range(N)]

cows.sort()

here_time = 0

for start, due_time in cows:
    here_time = max(here_time, start) + due_time

print(here_time)