T = int(input())
a = []
for _ in range(T):
    name, score = input().split()
    a.append((name,int(score)))

a.sort(key=lambda s: s[1])

for man in a:
    print(man[0], end=' ')