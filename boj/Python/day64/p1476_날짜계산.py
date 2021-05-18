E, S, M = map(int, input().split())

cnt = 1
while not (E==1 and S==1 and M==1):
    cnt += 1
    E = E-1 if E > 1 else 15
    S = S-1 if S>1 else 28
    M = M-1 if M>1 else 19

print(cnt)