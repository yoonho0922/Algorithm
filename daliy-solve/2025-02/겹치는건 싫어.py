# https://www.acmicpc.net/problem/20922

from collections import defaultdict

N, K = map(int, input().split())
S = list(map(int, input().split()))

d = defaultdict(int)
start, end, answer = 0, 0, 1
d[S[start]] = 1

while start < N - 1:
    while end < N - 1 and d[S[end + 1]] < K:
        end += 1
        d[S[end]] += 1
        answer = max(answer, end - start + 1)
    d[S[start]] -= 1
    start += 1

print(answer)