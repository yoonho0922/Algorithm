# https://www.acmicpc.net/problem/4358

import sys
readline = sys.stdin.readline

D = dict()
total = 0

while True:
    tree = readline().rstrip()
    if tree == '':
        break
    D.setdefault(tree, 0)
    D[tree] += 1
    total += 1

for name, cnt in sorted(D.items(), key=lambda x: x[0]): # 사전 순 정렬
    print(f"{name} {(100 * cnt / total):.4f}")