# https://www.acmicpc.net/problem/23971

import math

H, W, N, M = map(int, input().split())

res = math.ceil(W/(M+1)) * math.ceil(H/(N+1))
print(res)