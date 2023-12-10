import sys
readline = sys.stdin.readline

N = int(input())
s = [1]
i = 2
ans, flag = ['+'], True
for _ in range(N):
    # 3
    X = int(readline())

    while i <= X:
        ans.append('+')
        s.append(i)
        i += 1

    if s.pop() == X:
        ans.append('-')
    else:
        flag = False

if flag:
    for i in range(len(ans)):
        print(ans[i])
else:
    print('NO')