# https://www.acmicpc.net/problem/18310

import math

N = int(input())
H = list(map(int, input().split()))
H.sort()
mid = math.ceil(N/2) - 1
print(H[mid])