exp = input().strip()
index = -1
for i in range(len(exp)):
    if exp[i] == '-':
        index = i
        break
if index != -1:
    exp = exp.replace('-', '+')
    plus = sum(list(map(int, exp[:i].split('+'))))
    minors = sum(list(map(int, exp[i+1:].split('+'))))
    print(plus-minors)
else:
    print(sum(list(map(int, exp.split('+')))))
