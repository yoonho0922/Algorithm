import sys
from collections import deque

readline = sys.stdin.readline


# 루머를 믿는지 검사하는 함수
def believe(node):
    count = 0

    for neighbor in G[node]:
        if time[neighbor] > -1:
            count += 1

    # 주변인의 절반 이상이면 루머를 믿음
    if count >= (len(G[node][1:])) / 2:
        return True
    return False


# 1. 업데이트 된 루머인(deque pop) 중심으로 일반인 탐색
# 2. 탐색한 일반인의 주변인 탐색 후 업데이트 (deque push)
# 3. 업데이트가 없으면 종료 (deque empty)
def bfs():
    q = deque(diffuser)
    t = 0

    while q:
        t += 1

        for _ in range(len(q)):
            cur = q.popleft()  # 업데이트 된 루머인

            # 업데이트 된 루머인 주변의 일반인
            for next in G[cur]:
                if next == 0:
                    break
                # 일반인이 루머를 믿는지 검사
                if time[next] == -1 and believe(next):
                    q.append(next)

        for update in q:
            time[update] = t

    print(*time[1:])


N = int(input())
G = [[0]]  # 1부터 N 까지의 노드

for _ in range(N):
    G.append(list(map(int, readline().split())))

M = int(input())
diffuser = list(map(int, input().split()))  # 루머 유포자
time = [-1] * (N + 1)  # 루머인이 된 시간

for d in diffuser:
    time[d] = 0

bfs()
