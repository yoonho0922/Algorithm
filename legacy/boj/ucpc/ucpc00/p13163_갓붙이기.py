N=int(input())
for _ in range(N):
    name = list(input().split())
    print('god'+''.join(map(str,name[1:])))