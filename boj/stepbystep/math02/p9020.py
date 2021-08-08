import sys
readline = sys.stdin.readline
MAX_NUMBER=10001

prime = [True] * (MAX_NUMBER)
prime[0] = False
prime[1] = False

for i in range(int(MAX_NUMBER**0.5+1)):
    if prime[i]:
        for j in range(i+i, MAX_NUMBER, i):
            prime[j] = False

T = int(input())
for _ in range(T):
    N = int(readline())
    ans = 0

    for i in range(2, N//2 + 1):
        if prime[i] and prime[N-i]:
            ans=i

    print(ans, N-ans)

