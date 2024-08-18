# https://www.acmicpc.net/problem/1550

x16 = '0123456789ABCDEF'

number = str(input())
ans = 0
for i in range(len(number)):
    ans += x16.find(number[i]) * (16**(len(number)-i-1))
print(ans)