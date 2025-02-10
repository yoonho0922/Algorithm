# https://www.acmicpc.net/problem/22251

digits = [
    [1, 1, 1, 0, 1, 1, 1], # 0
    [0, 0, 1, 0, 0, 0, 1], # 1
    [0, 1, 1, 1, 1, 1, 0], # 2
    [0, 1, 1, 1, 0, 1, 1], # 3
    [1, 0, 1, 1, 0, 0, 1], # 4
    [1, 1, 0, 1, 0, 1, 1], # 5
    [1, 1, 0, 1, 1, 1, 1], # 6
    [0, 1, 1, 0, 0, 0, 1], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [1, 1, 1, 1, 0, 1, 1] # 9
]


def num_to_digit(num):
    digit = [0] * K
    for i in range(K):
        digit[i] = num % 10
        num //= 10
    return digit

def get_diff(cur_digit, target_digit):
    cnt = 0
    for i in range(K):
        for j in range(len(digits[0])):
            if digits[cur_digit[i]][j] != digits[target_digit[i]][j]:
                cnt += 1
    return cnt

N, K, P, X = map(int, input().split())

cur_digit = num_to_digit(X)
answer = 0

for i in range(1, N + 1):
    target_digit = num_to_digit(i)
    diff = get_diff(cur_digit, target_digit)
    if 0 < diff <= P:
        answer += 1

print(answer)
