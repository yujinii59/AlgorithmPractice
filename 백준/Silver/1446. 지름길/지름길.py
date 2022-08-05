from collections import deque

n, d = map(int, input().split())
roads = []
shortcuts = {}
for _ in range(n):
    s, e, dist = map(int, input().split())
    if e <= d and e-s > dist:
        if shortcuts.get((s,e), 0):
            if shortcuts[(s,e)] > dist:
                shortcuts[(s,e)] = dist
        else:
            shortcuts[(s,e)] = dist
            roads.append((s, e))
        
roads = sorted(roads)
q = deque()
q.append((0,0))
min_dist = d
while q:
    loc, dist = q.popleft()
    for i in range(len(roads)):
        start, end = roads[i]
        if loc == start:
            q.append((end, dist + shortcuts[(start, end)]))
        elif loc < start:
            q.append((start, dist + (start - loc)))
            break
        elif loc > start and i == len(roads)-1:
            min_dist = min(min_dist, dist + (d - loc))
print(min_dist)       