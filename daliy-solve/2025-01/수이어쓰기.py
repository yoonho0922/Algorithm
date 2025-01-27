# https://www.acmicpc.net/problem/1515

S = input()
index = 0
answer = 0

i = 1
while index < len(S):
    num = str(i)
    for j in range(len(num)):
        if index < len(S) and num[j] == S[index]:
            index += 1
            answer = i
    i += 1

print(answer)