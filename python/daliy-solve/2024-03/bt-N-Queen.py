# https://www.acmicpc.net/problem/9663

def is_promising(x):
    for i in range(x):
        # 같은 열에 다른 퀸이 있거나, 대각선에 다른 퀸이 있으면 False
        if locations[i]==locations[x] or abs(locations[x]-locations[i]) == abs(i-x):
            return False

    return True


def get_count(x):
    global cnt

    if x == N:
        cnt += 1
        return

    for i in range(N):
        locations[x] = i
        if is_promising(x):
            get_count(x+1)



N = int(input())
cnt = 0
locations = [0] * N

get_count(0)

print(cnt)