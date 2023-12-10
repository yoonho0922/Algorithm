from sys import stdin

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))

P.sort()

wait = 0
total_wait = 0

for i in P:
    wait += i
    total_wait += wait

print(total_wait)