# https://www.acmicpc.net/problem/2485

def get_gcd(a, b):
    if a % b == 0:
        return b
    tmp = b
    b = a % b
    a = tmp
    return get_gcd(a, b)



N = int(input())
dists = [int(input()) for _ in range(N)]
dists.sort()
gaps = []
for i in range(1, N):
    gaps.append(dists[i]-dists[i-1])

gcd = gaps[0]
for i in range(1, len(gaps)):
    gcd = get_gcd(gcd, gaps[i])

answer = 0
for g in gaps:
    answer += (g // gcd) - 1
print(answer)