# https://www.acmicpc.net/problem/21608

from collections import defaultdict

dy = [0,0,1,-1]
dx = [1,-1,0,0]


def set_student(G, student, likes):
    candi_like_count = -1
    candi_empty_count = -1
    candi = [] # 앉힐 자리

    # 앉힐 자리 구하기
    for i in range(N):
        for j in range(N):
            # 빈 자리가 아니면 무시
            if G[i][j] != 0:
                continue

            like_count = 0
            empty_count = 0

            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                # 인접 칸 빈자리 수, 호감 수 구하기
                if 0<=ny<N and 0<=nx<N:
                    if G[ny][nx] in likes:
                        like_count += 1
                    if G[ny][nx] == 0:
                        empty_count +=1

            # print(student, [i,j], like_count, empty_count)
            # 호감이 더 많거나, 호감이 같으면서 빈자리가 많다면 앉힐 자리 변경
            if (like_count > candi_like_count
                    or (like_count == candi_like_count and empty_count > candi_empty_count)):
                candi_like_count = like_count
                candi_empty_count = empty_count
                candi = [i, j]

    # 앉히기
    G[candi[0]][candi[1]] = student


def get_score(G, like_list):
    total = 0
    scores = [0,1,10,100,1000]

    for i in range(N):
        for j in range(N):
            student = G[i][j]
            like_count = 0

            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                # 인접 칸 빈자리 수, 호감 수 구하기
                if 0<=ny<N and 0<=nx<N and G[ny][nx] in like_list[student]:
                    like_count += 1
            total += scores[like_count]

    return total



N = int(input())
G = [[0]*(N) for _ in range(N)]
like_list = [[] for _ in range(N**2+1)]

for _ in range(N**2):
    row = list(map(int, input().split()))
    student, likes = row[0], row[1:]
    like_list[student] = likes

    set_student(G, student, likes)


# for i in range(N):
#     print(G[i])

score = get_score(G, like_list)
print(score)