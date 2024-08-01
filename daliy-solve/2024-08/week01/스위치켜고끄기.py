# https://www.acmicpc.net/problem/1244


def switch(s, index):
    if s[index]:
        s[index] = 0
    else:
        s[index] = 1


N = int(input())
S = [-1] + list(map(int, input().split())) # 입력 값이 첫 번째 부터 시작하도록 -1을 추가
M = int(input())

for _ in range(M):
    sex, num = map(int, input().split())
    if sex == 1:
        # num의 배수의 스위치들을 변경
        for i in range(num, N+1, num):
            switch(S, i)
    elif sex == 2:
        # num에 대해 좌우 대칭인 스위치들을 변경
        for gap in range(min(N-num+1, num)):
            if gap == 0:
                switch(S, num)
            elif S[num+gap] == S[num-gap]:
                switch(S, num+gap)
                switch(S, num-gap)
            else:
                break


for i in range(N//20 + 1):
    print(*S[i * 20 + 1 : i * 20 + 21])