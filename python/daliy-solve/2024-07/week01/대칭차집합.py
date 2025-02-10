# https://www.acmicpc.net/problem/1269

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

commons, ap, bp = 0, 0, 0

A.sort()
B.sort()

while ap<len(A) and bp<len(B):
    if A[ap] == B[bp]:
        commons += 1
        ap += 1
        bp += 1
    elif A[ap] > B[bp]:
        bp += 1
    else:
        ap += 1

print(len(A)+len(B)-commons*2)