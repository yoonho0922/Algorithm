# https://www.acmicpc.net/problem/4659

vowel  = ['a','e','i','o','u']

while True:
    s = input()

    if s == 'end':
        exit()

    cnt_v = 0
    continuous_v = 0
    continuous_c = 0

    for i in range(len(s)):
        if s[i] in vowel:
            continuous_v += 1
            continuous_c = 0
            cnt_v += 1
        else:
            continuous_c += 1
            continuous_v = 0

        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if continuous_v >=3 or continuous_c >= 3:
            print('<'+s+'> is not acceptable.')
            break

        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if i>0 and s[i] == s[i-1] and s[i] not in ('e','o'):
            print('<'+s+'> is not acceptable.')
            break
    else:
        # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        if cnt_v > 0:
            print('<'+s+'> is acceptable.')
        else:
            print('<'+s+'> is not acceptable.')
