# https://www.acmicpc.net/problem/1644

def eratos(maximum):
    prime = [True] * (maximum + 1)
    prime[0], prime[1] = False, False

    for i in range(2, int(maximum**0.5) + 1):
        if prime[i]:
            for j in range(i+i, maximum + 1, i):
                prime[j] = False

    return [i for i in range(2, maximum + 1) if prime[i]]

N = int(input())
primes = eratos(N)

ans, l, r, cur = 0, 0, 0, primes[0] if primes else 0

while r < len(primes):
    if cur == N:
        ans += 1
        l +=1
        r += 1
        if r < len(primes):
            cur += primes[r] - primes[l-1]
    elif cur < N:
        r += 1
        if r < len(primes):
            cur += primes[r]
    else : # cur > N
        l += 1
        cur -= primes[l-1]

print(ans)
