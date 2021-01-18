import sys
readline = sys.stdin.readline

N = int(readline())
words = []

for _ in range(N):
    word = readline().strip()
    words.append((word, len(word)))

words = list(set(words))
words.sort(key=lambda x: (x[1], x[0]))

for w in words:
    print(w[0])