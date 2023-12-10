def getSec(time, interval):
    h, m, s = map(float, time.split(':'))
    h, m, s = map(int, [h*1000, m*1000, s*1000])
    interval = int(float(interval[:len(interval) - 1])*1000)

    s = s + m*60 + h * 60 * 60
    return [s-interval+1, s]


def solution(lines):
    times = []
    for line in lines:
        l = list(line.split())
        times.append(getSec(l[1], l[2]))


    ans = 0

    for cur_s, cur_e in times:
        cnt1, cnt2 = 0, 0
        for s, e in times:
            # 한 시점의 시작부터 1초 동안 트래픽 확인
            if cur_s+999 >= s >= cur_s or cur_s <= e <= cur_s + 999\
                    or s<=cur_s<=e:
                cnt1 += 1
                # print(1, cnt1, cur_s, s, e)
            # 한 시점의 끝부터 1초 동안 트래픽 확인
            if cur_e+999 >= s >= cur_e or cur_e <= e <= cur_e + 999\
                    or s<=cur_e<=e:
                # print(2, cnt1, cur_s, s, e)
                cnt2 += 1
        ans = max([ans, cnt1, cnt2])
    return ans


print(solution(
    ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
))
