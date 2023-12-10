N=123456*2
prime = [True]*(N+1)
prime[0]=False
prime[1]=False

for i in range(2, int(N**0.5+1)):
    if prime[i]:
        for j in range(i+i, N+1, i):
            prime[j]=False

while True:
    X = int(input())
    if X==0:
        break
    ans = 0
    for i in range(X+1, X*2+1):
        if prime[i]:
            ans+=1
    print(ans)