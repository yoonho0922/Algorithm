from collections import deque

T = int(input())

## get prime number
prime = [True]*10001
for i in range(2, 5000):
    if prime[i] == True:
        for j in range(i+i, 10001, i):
            prime[j] = False

def bfs(s, e):

    queue.append(s)
    dist[s] = 1

    while queue:

        curr = queue.popleft()
        # 목적지 도착
        if curr == e:
            print(dist[B] - 1)
            return
        # 각 자리수 0~9로 변경
        for i in range(10):
            # 천의 자리 변경
            if i != 0:
                next = (curr%1000) + i*1000
                if prime[next] and dist[next] == 0:
                    dist[next] = dist[curr] + 1
                    queue.append(next)
            # 일의 자리 ~ 백의 자리 변경
            for j in range(3):
                next = curr//pow(10,j+1)*pow(10,j+1) + curr%pow(10,j) + i*pow(10,j)
                if prime[next] and dist[next] == 0:
                    dist[next] = dist[curr] + 1
                    queue.append(next)
    print('Impossible')

for _ in range(T):
    queue = deque()
    dist = [0]*10001
    A, B = map(int, input().split())
    bfs(A, B)