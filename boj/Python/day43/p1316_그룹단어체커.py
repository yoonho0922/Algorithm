import sys
readline = sys.stdin.readline

N = int(readline())
ans = 0
for _ in range(N):
    word = readline().strip()
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            continue
        if word[i] in word[:i]:
            break
    else:
        ans += 1
print(ans)