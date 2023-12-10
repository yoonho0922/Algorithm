import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    p, m, f, c = map(int, readline().split())

    cou = (m//p) * c # 쿠폰의 수
    r = cou % f
    bc = r + (cou // f) * c # 보너스 쿠폰의 수



    ans = 0

    # 보너스 쿠폰으로 또 시킬 수 있으면
    while bc >= f:
        # print(ans)
        ans += bc // f # 보너스 쿠폰으로 시킨 수
        r = bc % f # 시키고 남은 보너스 쿠폰

        bc = bc - (bc//f)*f + (bc // f) * c

    print(ans)