import sys
readline = sys.stdin.readline

N = int(readline())
distance = list(map(int, readline().split()))
costs = list(map(int, readline().split()))

totalCost = 0
curCost = costs[0]

for i in range(N - 1):

    totalCost += curCost * distance[i]

    if costs[i+1] < curCost:
        curCost = costs[i+1]

print(totalCost)
