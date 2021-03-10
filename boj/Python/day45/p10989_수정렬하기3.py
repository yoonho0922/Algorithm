# pypy3 계산 속도가 빠른 대신 더 많은 메모리를 사용함.
import sys
readline = sys.stdin.readline

N = int(input())
counts = dict()
for _ in range(N):
    num = int(readline())
    if counts.get(num):
        counts[num] += 1
    else:
        counts[num] = 1
for i in range(10001):
    if counts.get(i):
        for _ in range(counts[i]):
            print(i)