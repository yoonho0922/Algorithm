# https://www.acmicpc.net/problem/1052

def to_binary(num):
    result = []
    while num > 0:
        result.append(str(num % 2))
        num //= 2
    return ''.join(result[::-1]) if result else "0"

N, K = map(int, input().split())
num = N
answer = 0
while to_binary(num).count("1") > K:
    index = to_binary(num)[::-1].index("1")
    num += 2 ** index
    answer += 2 ** index
print(answer)
