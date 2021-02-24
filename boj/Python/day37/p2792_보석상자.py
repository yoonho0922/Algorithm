import math
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
jams = []
for _ in range(M):
    jams.append(int(readline()))

ans, left, right = 0, 1, max(jams)
while left <= right:
    mid = (left + right) // 2
    isWithin = True # 모든 보석을 줄 수 있는지 여부
    need_people = 0

    for jam in jams:
        need_people += math.ceil(jam/mid)
        if need_people > N:
            isWithin = False
            break

    if isWithin:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)