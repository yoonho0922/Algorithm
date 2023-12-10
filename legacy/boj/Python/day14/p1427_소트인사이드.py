import sys
readline = sys.stdin.readline

s = readline().strip()
s = list(map(int, s))
s.sort(reverse=True)
for i in s:
    print(i, end="")