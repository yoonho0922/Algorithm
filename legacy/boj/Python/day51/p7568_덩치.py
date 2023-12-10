import sys
readline = sys.stdin.readline
N = int(readline())
people = []
for _ in range(N):
    a, b = map(int, readline().split())
    people.append([a, b])
for i in range(len(people)):
    ans = 1
    for j in range(len(people)):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            ans += 1
    print(ans, end=' ')
