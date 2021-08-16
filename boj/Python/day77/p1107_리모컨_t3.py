N = input()
M = int(input())

wrong = [False]*10
if M>0:
    for i in list(map(int, input().split())):
        wrong[i] = True
else:
    print(abs(int(N)-100))
    exit()

# 채널 버튼 안누르는 경우
ans = abs(int(N)-100)

# 채널 버튼 누르는 경우
for i in range(1111111):
    # 고장난 버튼이 있는지 검사
    num = str(i)
    for j in range(len(num)):
        if wrong[int(num[j])]:
            break
        elif j == len(num)-1:
            ans = min(ans, abs(i-int(N))+len(num))

print(ans)