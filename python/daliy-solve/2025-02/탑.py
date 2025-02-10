# https://www.acmicpc.net/problem/2493

N = int(input())
tops = list(map(int, input().split()))
stack = [] # [높이, 위치: 0 부터 시작]
result = [0] * N

for i in range(N-1, -1, -1):
    while stack and tops[i] >= stack[-1][0]:
        height, index = stack.pop()
        result[index] = i + 1
    stack.append([tops[i], i])

print(' '.join(map(str,result)))