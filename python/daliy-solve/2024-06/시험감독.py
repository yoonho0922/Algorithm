# https://www.acmicpc.net/problem/13458

import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0

for students in A:
    if students <= B:
        ans += 1
    else:
        ans += 1 + math.ceil((students - B) / C)

print(ans)
