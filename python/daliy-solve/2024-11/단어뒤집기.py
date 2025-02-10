# https://www.acmicpc.net/problem/9093

N = int(input())
for _ in range(N):
    words = input().split()
    for word in words:
        print(word[::-1], end=' ')
