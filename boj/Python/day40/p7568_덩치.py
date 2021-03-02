import sys
readline = sys.stdin.readline

N = int(readline())
sizes = []
for _ in range(N):
    sizes.append(list(map(int, readline().split())))
ranks = []

for i in range(len(sizes)):
    rank = 1
    for j in range(len(sizes)):
        if sizes[j][0] > sizes[i][0] and sizes[j][1] > sizes[i][1]:
            rank += 1
    ranks.append(rank)
print(' '.join(list(map(str, ranks))))