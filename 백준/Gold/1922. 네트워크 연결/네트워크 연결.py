import heapq

def parents(num, conn):
    if num != conn[num]:
        conn[num] = parents(conn[num], conn)        
    return conn[num]


n = int(input())
conn = [i for i in range(n+1)]
q = []
m = int(input())
for _ in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(q, (cost, a, b))
    
costs = 0
while q:
    cost, a, b = heapq.heappop(q)
    p_a, p_b = parents(a, conn), parents(b, conn)
    if p_a < p_b:
        conn[p_b] = conn[p_a]
        costs += cost
    elif p_a > p_b:
        conn[p_a] = conn[p_b]
        costs += cost
        
print(costs)