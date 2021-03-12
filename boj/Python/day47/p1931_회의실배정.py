import sys
readline = sys.stdin.readline

N = int(readline())
confs = []
for _ in range(N):
    confs.append(list(map(int, readline().split())))
confs.sort(key=lambda x: (x[1], x[0]))
end_time, ans = 0, 0
for i in range(len(confs)):
    if confs[i][0] >= end_time:
        end_time = confs[i][1]
        ans += 1
print(ans)