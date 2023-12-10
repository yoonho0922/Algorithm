M = 1000
prime = [True]*(M+1)
prime[1] = False
for i in range(2, int(M**0.5)+1):
    if prime[i]:
        for j in range(i+i, M+1, i):
            prime[j] = False

N = int(input())
nums = list(map(int, input().split()))

ans = 0
for num in nums:
    if prime[num]:
        ans+=1
print(ans)
