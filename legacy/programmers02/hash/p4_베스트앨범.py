def solution(genres, plays):
    N = len(plays)
    answer = []

    g_rank = [] # [("classic", 1300), ...)
    m_rank = dict() # {"classic":[(100, 1), (19, 3), (300, 4)], ...}

    for i in range(N):
        cur_g = genres[i]
        m_rank[cur_g] = m_rank.get(cur_g, []) + [(plays[i], i)]

    for g in m_rank.keys():
        m_rank[g].sort(key=lambda x: (-x[0], x[1]))
        total_play = sum([play for play, _ in m_rank[g]])
        g_rank += [(total_play, g)]

    g_rank.sort(reverse=True)

    for _, g in g_rank:
        answer.extend([x for _, x in m_rank[g][:2]])

    return answer

print(solution(["classic", "pop", "rock", "classic", "classic", "pop", "rock"],
         [500, 600, 150, 3, 800, 2500, 3]))