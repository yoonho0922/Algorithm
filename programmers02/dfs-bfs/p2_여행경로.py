def dfs(s, visited, tickets, route):
    # print(len(route), route, s)
    if len(route) == len(tickets)+1:
        return route

    for i in range(len(tickets)):
        if not visited[i] and tickets[i][0] == s:
            visited[i] = True
            route.append(tickets[i][1])
            ans = dfs(tickets[i][1], visited, tickets, route)

            if ans:
                return ans

            route.pop()
            visited[i] = False


def solution(tickets):
    tickets.sort()
    return dfs("ICN", [False]*len(tickets), tickets, ["ICN"])



print(solution(
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"],
     ["ZAK", "JFK"], ["JFK", "ZAK"]]
))