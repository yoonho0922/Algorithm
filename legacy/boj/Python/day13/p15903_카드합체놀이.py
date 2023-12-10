import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
cards = list(map(int, readline().split()))
cards.sort()

for i in range(M):

    card_sum = cards[0] + cards[1]
    cards[0] = card_sum
    cards[1] = card_sum
    cards.sort()

print(sum(cards))