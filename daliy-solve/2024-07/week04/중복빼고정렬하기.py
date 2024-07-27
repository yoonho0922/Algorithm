# https://www.acmicpc.net/problem/10867

N = int(input())
s = set(map(int, input().split()))
print(' '.join(map(str, sorted(s))))