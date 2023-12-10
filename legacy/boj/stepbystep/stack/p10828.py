import sys
readline = sys.stdin.readline

T = int(readline())
s=[]
for _ in range(T):
    cmd = list(readline().split())

    if cmd[0]=='push':
        s.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if len(s)>0:
            print(s.pop())
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(s))
    elif cmd[0]=='empty':
        print(1 if len(s)==0 else 0)
    elif cmd[0]=='top':
        if len(s)>0:
            print(s[-1])
        else:
            print(-1)
