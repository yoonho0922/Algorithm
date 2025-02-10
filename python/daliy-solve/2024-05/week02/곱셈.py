# https://www.acmicpc.net/problem/1629

def sol(b):
    if b<=2:
        return A**b%C

    partialAns = sol(b//2)

    if b%2 == 1:
        return (partialAns * partialAns * A)%C
    else:
        return (partialAns * partialAns)%C


A, B, C = map(int, input().split())
print(sol(B))