num = input()
N = len(num)
M = int(input())
wrong = list(map(int, input().split()))

# 누를 수 있는 수 중 가장 큰 수와 작은 수
nw_max, nw_min = -1, 10
for i in range(10):
    if i in wrong:
        continue
    nw_max = max(nw_max, i)
    nw_min = min(nw_min, i)

# 숫자버튼 X
ans = abs(int(num)-100)

if M==10:
    print(ans)
    exit()

# 숫자버튼 사용

def get_top(bench):
    for i in range(bench+1, 10):
        if not(i in wrong):
            return i

def get_bot(place, bench):
    bot = 0
    for i in range(bench, -1, -1):
        if not(i in wrong) or (place==0 and i==0):
            return i

d = [[0]*N for _ in range(2)]
top, bot = False, False

for i in range(N):
    if int(num[i]) in wrong:
        # num[i] 보다 바로 큰 수
        if nw_max > int(num[i]):
            d[0][i] = get_top(int(num[i]))
            top=True
        # num[i] 보다 바로 작은 수
        if nw_min < int(num[i]) or (N>1 and i==0) or (N==2 and i==1):
            d[1][i] = get_bot(i, int(num[i]))
            bot=True

        for j in range(i+1, N):
            if top:
                d[0][j] = nw_min
            if bot:
                d[1][j] = nw_max
        break
    else:
        d[0][i] = int(num[i])
        d[1][i] = int(num[i])

if top:
    s1 = int(''.join(list(map(str, d[0]))))
    ans = min(ans, abs(int(num) - s1) + N)
    print(s1)
if bot:
    s2 = int(''.join(list(map(str, d[1]))))
    if d[1][0]==0 and N>1:
        ans = min(ans, abs(int(num) - s2) + N-1)
    else:
        ans = min(ans, abs(int(num) - s2) + N)
    print(s2)
print(ans)
