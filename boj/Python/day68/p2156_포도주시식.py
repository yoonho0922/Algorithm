def dp():
    for _ in range(N):
        p.append(int(input()))

    if N==1:
        return p[1]

    d = [0, p[1], p[1] + p[2]]

    for i in range(3, N + 1):
        d.append(max(d[i-1], d[i - 2] + p[i], d[i - 3] + p[i - 1] + p[i]))
    return max(d)

N = int(input())
p = [0]

print(dp())