import heapq

def solution(n, paths, gates, summits):
    conn = {i:[] for i in range(1, n+1)}
    for path in paths:
        a, b, cost = path
        conn[a].append((cost, b))
        conn[b].append((cost, a))

    intensity = {i:int(1e7) for i in range(1, n+1)}
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate))
        intensity[gate] = 0

    gates = {gate:0 for gate in gates}
    summits = set(summits)
    while q:
        time, loc = heapq.heappop(q)
        if intensity[loc] < time:
            continue
            
        if loc in summits:
            continue

        for cost, point in conn[loc]:
            max_time = max(time, cost)
            if gates.get(point, 1) and intensity[point] > max_time:
                intensity[point] = max_time
                heapq.heappush(q, (max_time, point))
    
    ls = []
    for summit in summits:
        ls.append([summit, intensity[summit]])
        
    ls = sorted(ls, key=lambda x: [x[1], x[0]])
    
    return ls[0]