# https://www.acmicpc.net/problem/12904

def tracking():
    here = T
    while here != '':
        if here == S:
            return 1

        if here[len(here) - 1] == 'A':
            here = here[:len(here) - 1]
        else:
            here = here[:len(here) - 1]
            here = here[::-1]

    return 0

S = input()
T = input()

print(tracking())
