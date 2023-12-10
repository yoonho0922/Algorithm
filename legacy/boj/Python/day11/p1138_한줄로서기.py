import sys
readline = sys.stdin.readline

N = int(readline())
arr = list(map(int, readline().split()))
result = [0]*N

for i in range(N):
    # i+1 번째 사람이 들어갈 자리
    j = 0

    while arr[i] > 0 or result[j] != 0:

        if result[j] == 0:
            arr[i] -= 1
            j += 1
        else:
            j += 1

    result[j] = i + 1

print(*result)