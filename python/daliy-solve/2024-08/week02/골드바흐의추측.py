# https://www.acmicpc.net/problem/6588
import sys
readline = sys.stdin.readline

MAX_NUMBER = 1_000_000

def get_prime():
    prime = [True] * (MAX_NUMBER+1)
    prime[0], prime[1] = False, False

    for i in range(2, MAX_NUMBER + 1):
        if prime[i]:
            for j in range(i + i, MAX_NUMBER+1, i):
                prime[j] = False

    return prime


is_prime = get_prime()

while True:
    N = int(readline())
    if N == 0:
        break
    for a in range(3, N-2):
        b = N-a
        if is_prime[a] and is_prime[b]:
            print('{} = {} + {}'.format(N, a, b))
            break