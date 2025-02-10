# https://www.acmicpc.net/problem/10799

S = input().rstrip()
N = len(S)

stack = []
ans = 0

for i in range(N):
    if S[i] == '(':
        stack.append(S[i])
    if S[i] == ')':
        # 레이저 일 경우 스택에서 하나를 제거한 만큼 막대가 추가됨
        if S[i-1] == '(':
            stack.pop() # 레이저 시작 부분 빼내기
            ans += len(stack)
        # 막대의 끝인 경우 해당 막대 하나만 추가됨
        else:
            stack.pop() # 막대 시작 부분 빼내기
            ans += 1

print(ans)