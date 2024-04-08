# https://www.acmicpc.net/problem/1105

L, R = map(str, input().split())

cnt = 0

# L, R 의 자릿 수 가 다르면 결과는 무조건 0
if len(L) == len(R):
    for i in range(len(L)):
        if L[i] != R[i]:
            break

        if L[i] == '8':
            cnt += 1

print(cnt)