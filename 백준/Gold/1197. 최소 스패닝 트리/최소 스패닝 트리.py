import heapq

def parents(point):
    if conn[point] != point:
        conn[point] = parents(conn[point])
        
    return conn[point]


v, e = map(int, input().split())
conn = [i for i in range(v+1)]
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

weight = 0    
while q:
    w, a, b = heapq.heappop(q)
    p_a = parents(a)
    p_b = parents(b)
    if p_a == p_b:
        continue
        
    if p_a < p_b:
        conn[b] = p_a
        conn[p_b] = p_a
    else:
        conn[a] = p_b
        conn[p_a] = p_b
        
    weight += w
print(weight)