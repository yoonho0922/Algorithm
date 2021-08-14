N, r, c = map(int, input().split())
ans = 0

def sol(num, depth, rc):
    global ans

    if depth > N:
        return

    u = num//pow(2, N-depth)
    if u>0:
        ans += u*rc*pow(2, 2*(N-depth))
        num = num%pow(2, N-depth)
    sol(num, depth+1, rc)

sol(r, 1, 2)
sol(c, 1, 1)
print(ans)