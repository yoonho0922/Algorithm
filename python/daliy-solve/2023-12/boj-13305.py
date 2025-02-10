# https://www.acmicpc.net/problem/13305
# 주유소

import sys
readline = sys.stdin.readline

N = int(readline())
dists = list(map(int, readline().split()))
nodes = list(map(int, readline().split()))

def get_node_rank():
    sorted_nodes = sorted(nodes)
    result = []
    for node in nodes:
        result.append(sorted_nodes.index(node))

    # print('debug result: ', result)
    return result

def solve():
    node_rank = get_node_rank()

    cost = 0

    i = 0
    while i<N-1:
        target_node = N

        for j in range(i+1, N):
            if node_rank[i]>node_rank[j]:
                target_node = j
                break
        # print('debug i target: ', i, target_node)

        cost += nodes[i] * sum(dists[i:target_node])
        i = target_node

    return cost

def get_cost(node_rank, start, cost):
    if start >= N-1:
        return cost

    end = N-1

    for j in range(start+1, N):
        if node_rank[start]>node_rank[j]:
            end = j
            break

    cost += nodes[start] * sum(dists[start:end])

    return get_cost(node_rank, end, cost)

def solve2():
    node_rank = get_node_rank()
    return get_cost(node_rank, 0, 0)

print(solve2())