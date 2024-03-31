# https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
A = list(map(int, input().split()))

now_sum = A[0]
cnt, start, end = 0, 0, 1

while end <= N:
    if now_sum == M:
        cnt += 1
        now_sum -= A[start]
        start += 1
    elif now_sum > M:
        now_sum -= A[start]
        start += 1
    else:
        if end < N:
            now_sum += A[end]
            end+=1
        else:
            break

print(cnt)