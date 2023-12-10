S = input()

jups = []

for i in range(len(S)):
    jups.append(S[i:])

jups.sort()

for j in jups:
    print(j)