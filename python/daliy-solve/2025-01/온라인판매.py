# https://www.acmicpc.net/problem/1246

N, M = map(int, input().split())
customers = [int(input()) for _ in range(M)]

max_payment = 0
max_price = 0


for i in range(M):
    price = customers[i]
    cnt = 0
    for j in range(M):
        if customers[j] >= price and cnt < N:
            cnt += 1
    payment = price * cnt
    if payment >= max_payment:
        max_payment = payment
        max_price = price

print(max_price, max_payment)