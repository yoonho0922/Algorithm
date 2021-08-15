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
L = len(N)
M = int(input())

# 잘못된 버튼이 없는 경우
if M==0:
    print(L)
    exit()

wrong = [False]*10

for i in list(map(int, input().split())):
    wrong[i]=True

ans = abs(int(N)-100)

d = []

for i in range(1, L+2):
    sol(0, i)

print(ans)