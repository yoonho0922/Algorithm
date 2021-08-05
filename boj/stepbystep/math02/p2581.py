N = int(input())
M = int(input())

prime=[True]*(M+1)
for i in range(2, int(M**0.5) + 1):
    if prime[i]:
        for j in range(i+i, M+1, i):
            prime[j]=False
prime[1]=False

S=[]

for i in range(N, M+1):
    if prime[i]:
        S.append(i)

if len(S)==0:
    print(-1)
else:
    print(sum(S))
    print(min(S))

