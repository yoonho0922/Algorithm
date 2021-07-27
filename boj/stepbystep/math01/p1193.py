x = int(input())
m, total = 0, 0
while True:
    if x > total + m + 1:
        m += 1
        total += m
    else:
        break
s = x - total
print(f"{s}/{m + 2 - s}" if (m + 1) % 2 == 0 else f"{m + 2 - s}/{s}")