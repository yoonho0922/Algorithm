# https://www.acmicpc.net/problem/2607

def count(word):
    counts = [0] * (ord('Z') - ord('A') + 1)
    for char in word:
        index = ord(char) - ord('A')
        counts[index] += 1
    return counts

N = int(input())
words = [input().strip() for _ in range(N)]
origin = count(words[0])
answer = 0

for word in words[1:]:
    more = 0
    less = 0
    target = count(word)

    for i in range(ord('Z') - ord('A') + 1):
        if target[i] > origin[i]:
            more += target[i] - origin[i]
        if target[i] < origin[i]:
            less += origin[i] - target[i]

    if more <= 1 and less <= 1:
        answer += 1

print(answer)