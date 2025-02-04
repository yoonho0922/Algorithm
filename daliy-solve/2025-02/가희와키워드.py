# https://www.acmicpc.net/problem/22233

import sys
readline = sys.stdin.readline

N, M = map(int, input().split())
memos = set([readline().strip() for _ in range(N)])
for _ in range(M):
    for word in readline().strip().split(','):
        memos.discard(word)
    print(len(memos))