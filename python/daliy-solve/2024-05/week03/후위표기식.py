#

# X(operand),+,-,'(': 스택에 보류, 특정 조건이나 값 읽기가 끝났을 경우 연산됨
# ')': '('가 나올때 까지 연산
# *,/: 다음 값이 '('이 아니 라면 연산

def integrate(a, operation, b):
    return a+b+operation

def calc_and_pop(stack, offset_condition):
    # stack의 첫번째는 무조건 operand임
    offset = len(stack)-1

    # offset은 index('(')+1 이거나 0임
    while offset>0:
        if stack[offset-1] in offset_condition:
            break
        offset -= 1

    res = stack[offset]

    for i in range(offset+1, len(stack), 2):
        operation, x = stack[i], stack[i+1]
        res = integrate(res, operation, x)

    for _ in range(len(stack)-offset):
        stack.pop()

    # print(res)
    return res


S = input()
stack = []

for i in range(len(S)):
    if S[i] == ')':
        # 후위연산 진행
        integration = calc_and_pop(stack, ['('])
        stack.pop() # '(' 제거
        stack.append(integration)
    elif S[i] in ['+','-','*','/','(']: # operation
        stack.append(S[i])
    else: # operand
        stack.append(S[i])
        if S[i-1] in ['*','/']:
            # 연산 처리
            integration = calc_and_pop(stack, ['+', '-', '('])
            stack.append(integration)

    while len(stack)>=2 and stack[-2] in ['*', '/'] and stack[-1] != '(':
        integration = calc_and_pop(stack, ['+', '-', '('])
        stack.append(integration)

print(calc_and_pop(stack, []))