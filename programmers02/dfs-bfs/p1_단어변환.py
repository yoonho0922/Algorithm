from collections import deque

def isNeighbor(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt+=1
    return cnt==1

def solution(begin, target, words):

    q = deque()
    visited = [False] * len(words)
    q.append(begin)

    ans = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == target:
                return ans

            for i in range(len(words)):
                if not visited[i] and isNeighbor(cur, words[i]):
                    q.append(words[i])
                    visited[i] = True
        ans += 1

    return 0

print(solution("hit",
               "cog",
               ["hot", "dot", "dog", "lot", "log", "cog"]))