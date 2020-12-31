import sys
input = sys.stdin.readline

def moja():
    mo, ja = 0, 0

    for char in pwd:
        # 모음이면
        if char in 'aeiou':
            mo += 1
        # 자음이면
        else:
            ja += 1
    # 최소 한개의 모음과 최소 두개의 자음이면
    if mo>0 and ja>1:
        return True
    return False

def dfs(s, d): # start, depth
    # 끝에 도달하면
    if d == L:
        # 조건을 만족하면
        if moja():
            for i in range(L):
                print(pwd[i], end='')
            print()
        return

    for i in range(s, len(chars)):
        pwd[d] = chars[i]
        dfs(i+1, d+1)

L, C = map(int, input().split())
chars = list(map(str, input().split()))
pwd = [0]*L
# mos = list(map(str, 'a e i o u'.split()))

chars.sort(key=lambda x:ord(x)) # 알파벳 순 정렬

dfs(0, 0)