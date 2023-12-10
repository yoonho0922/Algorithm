from collections import deque
from sys import stdin

prime = [True]*(10000)
# n-1 까지의 소수를 구함
def get_prime(n):
    for i in range(2, int(n**0.5)):
        if prime[i]:
            for j in range(i+i, n, i):
                prime[j] = False

# n-1 까지의 소수중에 탐색
def bfs(n, s, e):
    ## init
    q = deque()
    d = [0] * n

    q.append(s)
    d[s] = 1

    while q:
        curr = q.popleft()
        # 목적지에 도달하면
        if curr == e:
            print(d[e]-1)
            return
        # 각 자리수를 0~9로 변경
        for i in range(10):
            # 천의 자리 변경
            if i != 0:
                next = curr % pow(10, 3) + i * pow(10, 3)
                # 방문하지 않은 소수라면
                if prime[next] and d[next] == 0:
                    d[next] = d[curr] + 1
                    q.append(next)
            # 일의 자리 ~ 백의 자리 변경
            for j in range(3):
                next = curr//pow(10,j+1)*pow(10,j+1) + curr%pow(10,j) + i*pow(10,j)
                # 방문하지 않은 소수라면
                if prime[next] and d[next] == 0:
                    d[next] = d[curr] + 1
                    q.append(next)

    print('Impossible')
    return

get_prime(10000)
T = int(input())
for _ in range(T):
    line = list(map(int, stdin.readline().split()))
    bfs(10000, line[0], line[1])