lyric = [
    'baby','sukhwan','tururu','turu',
    'very','cute', 'tururu','turu',
    'in','bed','tururu','turu',
    'baby', 'sukhwan'
]

N = int(input())
N -=1
if N%14 in [2,6,10]:
    if N>41:
        print('tu+ru*{}'.format(N//14+2))
    else:
        print('tururu'+'ru'*(N//14))
elif N%14 in [3,7,11]:
    if N > 55:
        print('tu+ru*{}'.format(N // 14 + 1))
    else:
        print('turu' + 'ru'*(N // 14))
else:
    print(lyric[N%14])