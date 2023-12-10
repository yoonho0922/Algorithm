N = int(input())
T = []
max = 0

for i in range(N):
    T.append(list(map(int, input().split())))

# 끝나는 순으로 정렬, 끝나는 시간이 같다면 시작 순으로 정렬
T.sort(key=lambda x: (x[1],x[0]))

prev = 0

for s, e in T:
    if(prev <= s):
        prev = e
        max += 1

print(max)