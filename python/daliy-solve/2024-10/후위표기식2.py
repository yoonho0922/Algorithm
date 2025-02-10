# https://www.acmicpc.net/problem/1935

alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
operators = "+-/*"

def operate(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "/":
        return x / y
    if op == "*":
        return x * y

N = int(input())
S = input()
nums = [int(input()) for _ in range(N)]
stack = []

for op in S:
    if op in operators:
        y = stack.pop()
        x = stack.pop()
        result = operate(x, y, op)
        stack.append(result)
    else:
        index = alphas.index(op)
        stack.append(nums[index])

print(f"{stack[0]:.2f}")
