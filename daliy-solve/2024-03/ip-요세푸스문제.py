# https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())

numbers = [i for i in range(N)]
visited = [False] * N
result = []

i = 0
count_down = K

while len(result) < N:
    if not visited[i]:
        count_down -= 1

    if count_down == 0:
        count_down = K
        result += [numbers[i] + 1]
        visited[i]=True

    i = (i+1)%N

print('<'+' ,'.join(map(str, result))+'>')