cros = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for c in cros:
    word = word.replace(c, '*')
print(len(word))