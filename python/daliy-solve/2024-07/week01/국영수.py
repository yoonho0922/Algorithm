# https://www.acmicpc.net/problem/10825

import sys
readline = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    name, kr, en, math = input().split()
    scores.append([name, int(kr), int(en), int(math)])

for name, _, _, _ in sorted(scores, key= lambda x: [-x[1], x[2], -x[3], x[0]]):
    print(name)
