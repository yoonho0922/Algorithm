# https://www.acmicpc.net/problem/20310

S = input()
cnt = [0] * 2

indices = [[], []]
for i in range(len(S)):
    if S[i] == '0':
        indices[0].append(i)
    else:
        indices[1].append(i)
# 0은 앞에서 부터 절반만 남기고, 1은 뒤에서 부터 절반만 남긴다.
indices[0] = indices[0][:len(indices[0])//2]
indices[1] = indices[1][len(indices[1])//2:]

union = []
for char in [0, 1]:
    for idx in indices[char]:
        union.append([idx, char])
union.sort(key=lambda x: x[0])

print(''.join(str(char) for _, char in union))