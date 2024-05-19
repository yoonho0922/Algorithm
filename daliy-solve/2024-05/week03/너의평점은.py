# https://www.acmicpc.net/problem/25206

N = 20

scores = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total = 0
times = 0

for _ in range(N):
    _, t, s = input().split()
    if s != 'P':
        total += float(t) * float(scores[s]) * 10
        times += float(t)


print((total * 1000 // times)/10000)
