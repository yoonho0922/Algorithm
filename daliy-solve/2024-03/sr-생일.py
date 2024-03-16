# https://www.acmicpc.net/problem/5635

import sys
readline = sys.stdin.readline

N = int(readline())
births = []
for _ in range(N):
    name, day, month, year = readline().split()
    births.append([name, int(day), int(month), int(year)])

# 생일 순으로 오름차순 정렬
births.sort(key=lambda x: (x[3],x[2],x[1]))

print(births[-1][0])
print(births[0][0])