import heapq

n, m, k, x = map(int, input().split())
conn = {i+1:[] for i in range(n)}
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    conn[a].append(b)
    
q = [(0, x)]
k_dist = set()
while q:
    dist, city = heapq.heappop(q)
    if visited[city] == 0:
        visited[city] = 1
        if dist == k:
            k_dist.add(city)
        elif dist > k:
            break

        else:
            for c in conn[city]:
                heapq.heappush(q, (dist+1, c))

if k_dist:
    print(*sorted(k_dist), sep='\n')
else:
    print(-1)