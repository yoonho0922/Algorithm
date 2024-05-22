# https://www.acmicpc.net/problem/1141

# 1. 문자열 정렬
# 2. 문자 길이를 늘려가며 섬사.
# 3. 문자열이 끝나는 지점에서 주변에 자신을 접두어로 갖는 문자열이 있으면 탈락
# 증명.
# 문자열 A와 AB가 있을때, 만약 AB를 접두어로 사용하는 문자열 X는 A를 접두어로 사용하는 문자열이기도 하므로
# A와 AB중 AB를 제거해야 최대 부분집합을 갖는 경우는 없음.

N = int(input())
S = [input() for _ in range(N)]
S.sort()

ans = N

for i in range(N-1):
    if S[i] == S[i+1][:len(S[i])]:
        ans -= 1

print(ans)