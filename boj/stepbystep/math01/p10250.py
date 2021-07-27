T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    x = int((N-1)/H) + 1
    y = N%H if N%H!=0 else H
    print(f'{y*100+x}')