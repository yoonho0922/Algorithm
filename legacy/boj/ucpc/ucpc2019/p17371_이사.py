import sys
readline = sys.stdin.readline

def distance(a,b,c,d):
    return (a-c)**2 + (b-d)**2

N = int(readline())
F = [] # facility
for _ in range(N):
    F.append(list(map(int, readline().split())))

d_min = 9876543210
d_min_idx = 0

for i in range(N): # 이사할 위치 F[i][0], F[i][1]
    far = -1 # 가장 먼 편의시설의 거리
    far_idx = 0

    for j in range(N):
        d = distance(F[i][0],F[i][1],F[j][0],F[j][1])
        if far < d:
            far = d
            far_idx = j

    if far < d_min:
        d_min = far
        d_min_idx = i


print(F[d_min_idx][0], F[d_min_idx][1])