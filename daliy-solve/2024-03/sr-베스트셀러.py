# https://www.acmicpc.net/problem/1302

from collections import defaultdict
import sys
readline = sys.stdin.readline

N = int(readline())
dict = defaultdict(int,key=0)

for _ in range(N):
    book = readline().rstrip()
    dict[book] += 1

# value는 내림차순, key는 오름차순으로 정렬
sorted_dict = sorted(list(dict.items()), key=lambda x: (-x[1],x[0]))

print(sorted_dict[0][0])