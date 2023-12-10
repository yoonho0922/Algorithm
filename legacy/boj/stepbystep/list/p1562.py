import sys
readline = sys.stdin.readline

ans, idx = -1, 1
for i in range(1, 10):
    num = int(readline())
    if num > ans:
        ans = num
        idx = i

print(ans)
print(idx)