import itertools

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

members = list(itertools.combinations(range(N), N//2))
t1 = members[:len(members)//2]
t2 = members[len(members)//2:]
t2.reverse()

ans = 1000000000

for i in range(len(t1)):
    t1_val = 0
    t2_val = 0

    for comb in list(itertools.combinations(t1[i], 2)):
        t1_val += S[comb[0]][comb[1]]
        t1_val += S[comb[1]][comb[0]]

    for comb in list(itertools.combinations(t2[i], 2)):
        t2_val += S[comb[0]][comb[1]]
        t2_val += S[comb[1]][comb[0]]

    ans = min(ans, abs(t1_val-t2_val))

print(ans)