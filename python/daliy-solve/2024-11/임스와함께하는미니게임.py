# https://www.acmicpc.net/problem/25757

N, game = input().split()
s = set()
for _ in range(int(N)):
    s.add(input())
if game == 'Y':
    print(len(s))
elif game == 'F':
    print(len(s)//2)
elif game == 'O':
    print(len(s)//3)
else:
    raise Exception