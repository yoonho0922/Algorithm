import sys
readline = sys.stdin.readline

s = readline()

change=[]

for i in range(1, len(s) - 1):
    if s[i] != s[i-1]:
        change.append(i)

if (len(change) % 2) == 1:
    print(len(change)//2 + 1)
else:
    print(len(change)//2)