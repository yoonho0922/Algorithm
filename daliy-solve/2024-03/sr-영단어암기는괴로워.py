# https://www.acmicpc.net/problem/20920

import sys
import collections
readline = sys.stdin.readline

N, M = map(int, readline().split())
words = [readline().rstrip() for _ in range(N)]

filtered_dict = collections.Counter(w for w in words if len(w)>=M)

for w, cnt in sorted(filtered_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(w)
