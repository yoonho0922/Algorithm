N = int(input())
G = [list(input()) for _ in range(N)]

f = [x for x in zip(*G)][::-1]

for i in range(N):
    print(''.join(map(str,f[i])))