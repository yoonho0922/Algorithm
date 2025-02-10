# http://acmicpc.net/problem/2668

N = int(input())
G = [0] * (N + 1)
for i in range(1, N + 1):
    G[i] = int(input())

set_a = set()
set_b = set()

def set_matched():
    for x in set_a:
        if x not in set_b:
            return False
    return True

def dfs(x):
    set_a.add(x)
    set_b.add(G[x])
    if set_matched():
        return True
    else:
        if G[x] not in set_a and G[G[x]] not in set_b and dfs(G[x]):
            return True
        else:
            set_a.remove(x)
            set_b.remove(G[x])
            return False


for i in range(1, N + 1):
    if i not in set_a and G[i] not in set_b:
        dfs(i)

print(len(set_b))
print('\n'.join(map(str,sorted(set_b))))