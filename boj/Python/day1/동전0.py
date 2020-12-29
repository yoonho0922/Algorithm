N, K = map(int, input().split())
coins = []
num = 0

for i in range(N):
    coins.append(int(input()))

# 내림차순으로 정렬
coins.sort(reverse=True)

for coin in coins:
    if(coin<=K):
        num += int(K/coin)
        K = K % coin

print(num)