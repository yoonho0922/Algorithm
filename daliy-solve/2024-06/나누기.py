# https://www.acmicpc.net/problem/1075

N = input()
M = int(input())

for i in range(100):
    added = str(i)
    if i < 10:
        added = str('0') + added
    if int(N[:-2] + added) % M == 0:
        print(added)
        break
