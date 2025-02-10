# https://www.acmicpc.net/problem/20006

N, max_room_size = map(int, input().split())
rooms = [] # e: Map<방장 레벨, 현재 인원>
participants = [] # e: List<Map<레벨, 닉네임>>
for _ in range(N):
    line = input().split()
    user_level, user_name = int(line[0]), line[1]
    # 방 탐색
    for i in range(len(rooms)):
        room_level = rooms[i][0]
        room_size = rooms[i][1]
        if room_size < max_room_size and room_level - 10 <= user_level <= room_level + 10:
            rooms[i][1] += 1
            participants[i].append([user_level, user_name])
            break
    # 입장 가능한 방 없으면 생성
    else:
        rooms.append([user_level, 1])
        participants.append([[user_level, user_name]])
# 방 정보 출력
for i in range(len(rooms)):
    if rooms[i][1] == max_room_size:
        print("Started!")
    else:
        print("Waiting!")
    participants[i].sort(key=lambda x: x[1])
    for level, name in participants[i]:
        print(level, name)