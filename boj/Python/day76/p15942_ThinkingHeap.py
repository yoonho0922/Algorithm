import sys
sys.setrecursionlimit(1000000)

def print_ans():
    for i in range(1, N+1):
        print(H[i])

def tracking(node):
    # print(node)
    if node == N+1:
        print_ans()
        exit()

    parent = H[node//2]

    if node == P:
        if K > parent:
            tracking(node + 1)
        else:
            return

    for i in range(1, N+1):
        if not visited[i] and i > parent:
            H[node] = i
            visited[i] = True
            tracking(node+1)
            visited[i] = False


N = int(input())
K, P = map(int, input().split())

H = [-1]*(N+1)
visited = [False]*(N+1) # 방문한 숫자

H[P] = K
visited[K]=True

tracking(1)
print(-1)