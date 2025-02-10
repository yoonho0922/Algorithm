# https://www.acmicpc.net/problem/11478

S = input()
part = set()

for size in range(1, len(S)+1): # 부분 문자열의 크기
    for i in range(len(S)): # 부분문자열의 시작점
        part.add(S[i:i+size])

print(len(part))