import sys
readline = sys.stdin.readline

N = int(readline())
weights = list(map(int, readline(). split()))
weights.sort()

sum_w = 0

for i in range(N):
    if sum_w + 1 >= weights[i]:
        sum_w += weights[i]
    else:
        break

print(sum_w+1)