# https://www.acmicpc.net/problem/1283


def check_put(keys, char):
    candi = str.upper(char)
    if candi not in keys:
        keys.add(candi)
        return True
    else:
        return False

T = int(input())
keys = set()
for _ in range(T):
    option = input()
    key_index = -1
    # 1. 단어 첫 글자 단위 검사
    for i in range(len(option)):
        if option[i] != " " and i == 0 or option[i-1] == " ":
            if check_put(keys, option[i]):
                key_index = i
                break
    # 2. 전체 문자 단위 검사
    else:
        for i in range(len(option)):
            if option[i] != " " and check_put(keys, option[i]):
                key_index = i
                break
    # 출력
    for i in range(len(option)):
        if i == key_index:
            print("[", option[i], "]",  sep="", end="")
        else:
            print(option[i], end="")
    print()
