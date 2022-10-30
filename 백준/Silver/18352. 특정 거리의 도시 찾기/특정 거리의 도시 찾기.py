import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, start, target, distance):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, curr = heappop(queue)
        if distance[curr] < dist:
            continue

        for node, d in graph[curr]:
            cost = dist + d
            if cost < distance[node]:
                distance[node] = cost
                heappush(queue, (cost, node))

    result = [i for i, fin_dist in enumerate(distance) if fin_dist == target]

    return result

n, m, k, x = map(int, input().split())
INF = int(1e9)

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append([v, 1])

result = dijkstra(graph, x, k, distance)
if len(result) == 0:
    print(-1)
else:
    print(*sorted(result), sep='\n')
