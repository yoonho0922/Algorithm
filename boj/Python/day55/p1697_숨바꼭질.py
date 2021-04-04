from collections import  deque

def bfs(start, target):
    visited = [False]*100001
    q = deque()
    q.append(start)
    ans = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == target:
                return ans
            for next in [cur-1, cur+1, cur*2]:
                if 0<=next<=100000 and not visited[next]:
                    q.append(next)
                    visited[next] = True
        ans += 1


N, K = map(int, input().split())
print(bfs(N, K))