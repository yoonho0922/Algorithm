# https://www.acmicpc.net/problem/1522

S = input()
N = len(S)

na = S.count('a')
answer = 1000
S = S + S # aabbbba 케이스를 확인하기 위해 이어 붙힘
for i in range(N):
    cnt = S[i:i+na].count('b')
    answer = min(answer, cnt)
print(answer)
