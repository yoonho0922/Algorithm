# https://www.acmicpc.net/problem/2525

h, m = map(int, input().split())
duration = int(input())

nm = (m + duration % 60)
nh = (h + duration // 60) % 24
if nm >= 60:
    nm %= 60
    nh = (nh + 1) % 24

print(nh, nm)