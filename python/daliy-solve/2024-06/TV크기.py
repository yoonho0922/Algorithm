# https://www.acmicpc.net/problem/1297

D, H, W = map(int, input().split())

a = int((D / ((H**2 + W**2) ** 0.5)) * H)
b = int((D / ((H**2 + W**2) ** 0.5)) * W)

print(a, b)