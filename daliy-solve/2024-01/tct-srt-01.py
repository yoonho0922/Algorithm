T = int(input())
a = []
for _ in range(T):
    a.append(int(input()))

print(*sorted(a, reverse=True))