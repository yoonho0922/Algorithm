a, b, c, d, e, f = map(int, input().split())

ta = a * d; tb = b * d; tc = c * d
td = d * a; te = e * a; tf = f * a

y = (tc-tf) // (tb-te)
if not a == 0:
    x = (c - b*y) // a
else:
    x = (f - e*y) // d
print(x, y)