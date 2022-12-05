import heapq

n = int(input())
times = sorted([list(map(int, input().split())) for _ in range(n)])
q = []
i = 0
time = 0
while i < n:
    s, t= times[i]
    i += 1
    time = s
    heapq.heappush(q, (t, s))
    while q:
        term, start = heapq.heappop(q)
        time += term
        j = i
        for j in range(i, n):
            s, t = times[j]
            if s <= time:
                heapq.heappush(q, (t, s))
            else:
                i = j
                break
    
        else:
            if i != n:
                i = j+1
            
print(time)  