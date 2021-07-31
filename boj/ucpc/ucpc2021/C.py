A, D, K = map(int, input().split())
d = [0, D/100] # 승률
p = [1, D/100] # 누적 확률
l = [1, (1-D/100)] # 누적 질 확률

i = 2
while d[-1] < 1:
    win = d[i-1] + d[i-1]*(K/100)
    if win >=1:
        win = 1
    d.append(win)
    l.append(l[i-1]*(1-d[i]))
    p.append( l[i-1] * d[i] ) # 전전의 누적 패배확률, 전에 패배할 확률, 지금 이길확률
    i+=1

ans = 0
p_total = 0

for i in range(1, len(d)):
    p_total += p[i]
    ans += i * p[i] * A
print('{:.7f}'.format(ans))