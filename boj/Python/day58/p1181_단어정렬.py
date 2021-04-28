import sys
readline = sys.stdin.readline

N = int(readline())
words = []
for _ in range(N):
    words.append(readline().strip())
words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)