cros = {
    'c=':1,
    'c-':1,
    'dz=':1,
    'd-':1,
    'lj':1,
    'nj':1,
    'nj':1,
    's=':1,
    'z=':1
}

word = input()
ans = 0
i = 0
while i < len(word):
    if i < len(word) - 2:
        c = word[i:i + 3]
        if cros.get(c):
            ans += 1
            i += 3
            continue
    if i < len(word) - 1:
        c = word[i:i + 2]
        if cros.get(c):
            ans += 1
            i += 2
            continue
    ans += 1
    i += 1
print(ans)