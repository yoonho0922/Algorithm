N = int(input())


prime = [True]*(N+1)

for i in range(2, N+1):
    if prime[i]:
        for j in range(i+i, N+1, i):
            prime[j]=False

x, idx= N, 2

while x>1:
    if prime[idx] and x%idx==0:
        print(idx)
        x = x//idx
    else:
        idx +=1