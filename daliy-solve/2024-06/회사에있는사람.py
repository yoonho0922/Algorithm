# https://www.acmicpc.net/problem/7785

import sys
readline = sys.stdin.readline

from collections import defaultdict

N = int(input())
D = defaultdict(bool)

for _ in range(N):
    name, action = readline().rstrip().split()
    if action == 'enter':
        D[name] = True
    else:
        D.pop(name)

for name in sorted(D.keys(), reverse=True):
    print(name)