# https://www.acmicpc.net/problem/11728

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(' '.join(map(str,sorted(A + B))))