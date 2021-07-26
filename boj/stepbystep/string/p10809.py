word=input()
d = [-1]*26
for i, x in enumerate(word):
    if d[ord(x)-97]!=-1:
        continue
    d[ord(x)-97]=i
print(*d)