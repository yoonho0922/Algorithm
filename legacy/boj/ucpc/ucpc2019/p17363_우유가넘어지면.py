def rotation(cur):
    if cur == '-':
        cur = '|'
    elif cur == '|':
        cur = '-'

    elif cur == '/':
        cur = '\\'
    elif cur == '\\':
        cur = '/'

    elif cur == '^':
        cur = '<'
    elif cur == '<':
        cur = 'v'

    elif cur == 'v':
        cur = '>'
    elif cur == '>':
        cur = '^'

    return cur

N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

for i in range(M-1, -1, -1):
    for j in range(N):
        c = rotation(S[j][i])

        print(c, end='')
    print()