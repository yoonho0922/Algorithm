def sol(depth, length):
    global ans

    if depth == length:
        cur = int(''.join(map(str, d)))
        ans = min(ans, abs(int(N)-cur) + length)
        return

    for i in range(10):
        if not wrong[i]:
            d.append(i)
            sol(depth+1, length)
            d.pop()


N = input()
M = int(input())
wrong = [False]*10
if M>0:
    for i in list(map(int, input().split())):
        wrong[i]=True

# 채널 버튼 안 누르는 경우
ans = abs(int(N)-100)

# 채널 버튼 누르는 경우
d = []
for i in range(1, len(N)+2):
    sol(0, i)

print(ans)