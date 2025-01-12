# https://www.acmicpc.net/problem/2212

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

gaps = []
for i in range(1, N):
    gaps.append(sensors[i] - sensors[i-1])
gaps.sort(reverse=True)

answer = sensors[N - 1] - sensors[0]

for i in range(min(len(gaps), K - 1)):
    answer -= gaps[i]

print(answer)