# https://www.acmicpc.net/problem/3507

n = int(input())
answer = 0
for i in range(100):
    for j in range(100):
        if i + j == n:
            answer += 1
print(answer)