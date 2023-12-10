i = 1
while True:
    L, P, V = map(int, input().split())
    if [L, P, V] == [0,0,0]:
        break

    ans = V // P * L
    if V % P <= L:
        ans += V % P
    else:
        ans += L
    print("Case {}:".format(i), ans)
    i += 1