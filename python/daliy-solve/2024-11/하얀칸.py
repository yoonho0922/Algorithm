# https://www.acmicpc.net/problem/1100

N = 8
ans = 0

for i in range(N):
    line = input()

    if i % 2 == 0:
        start_index = 0
    else:
        start_index = 1

    for j in range(start_index, N, 2):
        if line[j] == 'F':
            ans += 1

print(ans)