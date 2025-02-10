# https://www.acmicpc.net/problem/1439
# 뒤집기

import sys
readline = sys.stdin.readline

s = input()


def flip(target_number):
    count = 0
    numbers = s

    i = 0
    while i < len(numbers):
        # 뒤집어야 하는 경우
        if numbers[i] != target_number:
            count += 1

            for j in range(i+1, len(numbers)):
                if numbers[j] == target_number:
                    i = j
                    break
            else:
                i = len(numbers)
        # 뒤집을 필요 없는 경우
        else:
            i += 1

    return count



print(min(flip('0'), flip('1')))