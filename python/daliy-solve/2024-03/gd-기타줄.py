# https://www.acmicpc.net/problem/1049

import sys
readline = sys.stdin.readline

N, M = map(int, input().split())
min_six_prices, min_single_prices = zip(*(map(int, input().split()) for _ in range(M)))
min_six_price, min_single_price = min(min_six_prices), min(min_single_prices)

if min_six_price < min_single_price * 6:
    # 6으로 나눈 나머지가 있는지에 따른 분기?
    # -> 6으로 나누어 떨어진다면 min_single_price * 0 이므로 더해질 값이 없음
    print(
        min_six_price * (N//6) + min(min_six_price, min_single_price * (N%6))
    )
else:
    print(min_single_price * N)