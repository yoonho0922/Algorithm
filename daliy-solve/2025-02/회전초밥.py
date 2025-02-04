# https://www.acmicpc.net/problem/2531

from collections import defaultdict
import sys
readline = sys.stdin.readline


def unique(coupon:int, s:defaultdict):
    cnt = 1 # 쿠폰으로 먹는 음식
    for key, value in s.items():
        if value > 0 and key != coupon:
            cnt += 1
    return cnt


# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, D, K, C = map(int, input().split())
foods = [int(readline()) for _ in range(N)]

kinds = defaultdict(int)
for i in range(K):
    kinds[foods[i]] += 1
answer = unique(C, kinds)

for i in range(1, N):
    kinds[foods[i-1]] -= 1
    kinds[foods[(i+K-1) % N]] += 1
    answer = max(answer, unique(C, kinds))

print(answer)