# https://www.acmicpc.net/problem/2023

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def dfs(num, depth):
    if not is_prime(num):
        return

    if depth == N:
        print(num)

    for i in range(10):
        dfs(int(str(num) + str(i)), depth+1)

N = int(input())

for i in [2, 3, 5, 7]:
    dfs(i, 1)