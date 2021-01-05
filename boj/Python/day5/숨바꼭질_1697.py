from collections import deque
def bfs(s, e):
    time = 0
    q, v = deque(), [0]*100001 # queue, visited
    q.append(s)
    v[s] = 1
    while q:
        # 현재 큐에 있는 모든 요소 검사
        for _ in range(len(q)):
            curr = q.popleft()
            # 목적지에 도달하면
            if curr == e:
                return time
            # 세 가지 방법을 검사
            for next in (curr+1, curr-1, curr*2):
                # 범위를 넘지 않고 next 를 방문하지 않았다면
                if 0<=next<=100000 and v[next]==0:
                    q.append(next)
                    v[next] = 1
        time += 1
#입력
N, K = map(int, input().split())
print(bfs(N, K))