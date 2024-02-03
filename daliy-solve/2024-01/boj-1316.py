# https://www.acmicpc.net/problem/1316
# 그룹단어

def check_group(word):
    for i in range(1,len(word)):
        if word[i]==word[i-1]:
            continue
        if word[i] in word[:i]:
            return False
    return True

T = int(input())
total = 0

for i in range(T):
    word = input()
    if check_group(word):
        total+=1

print(total)