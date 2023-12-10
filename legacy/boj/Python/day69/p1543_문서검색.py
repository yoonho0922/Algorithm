doc = input()
word = input()
ans, i = 0, 0

while i < len(doc):
    if doc[i:i+len(word)] == word:
        ans += 1
        i += len(word)
    else:
        i += 1

print(ans)