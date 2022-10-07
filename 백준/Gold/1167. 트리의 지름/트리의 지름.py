import heapq
import sys

input = sys.stdin.readline

n = int(input())
conn = {i+1:[] for i in range(n)}
for _ in range(n):
    infos = list(map(int, input().split()))
    num, infos = infos[0], infos[1:-1]
    l = len(infos)
    for i in range(0,l,2):
        conn[num].append(infos[i:i+2])
        
q = []
heapq.heappush(q, (0, 1))
visited = [-1]*(n+1)
max_node = 1
max_dist = 0
while q:
    dist, node = heapq.heappop(q)
    visited[node] = -dist
    if max_dist < -dist:
        max_dist = -dist
        max_node = node
    for p, d in conn[node]:
        if visited[p] == -1:
            heapq.heappush(q, (dist-d, p))

heapq.heappush(q, (0, max_node))
visited = [-1]*(n+1)
while q:
    dist, node = heapq.heappop(q)
    visited[node] = -dist
    for p, d in conn[node]:
        if visited[p] == -1:
            heapq.heappush(q, (dist-d, p))
print(max(visited))