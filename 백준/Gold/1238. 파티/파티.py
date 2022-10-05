import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
roads = {i+1:[] for i in range(n)}
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((c, b))
    
times = [0] * (n+1)
for i in range(1, n+1):
    if i == x:
        hq = []
        heapq.heappush(hq, (0, i))
        visited = [0] * (n+1)
        while hq:
            time, loc = heapq.heappop(hq)
            if visited[loc] == 0:
                times[loc] += time
                visited[loc] = 1
                for cost, to in roads[loc]:
                    if visited[to] == 0:
                        heapq.heappush(hq, (time+cost, to))
    else:
        hq = []
        heapq.heappush(hq, (0, i))
        visited = [0] * (n+1)
        while hq:
            time, curr = heapq.heappop(hq)
            if curr == x:
                times[i] += time
                break
                
            if visited[curr] == 0:
                visited[curr] = 1
                for cost, to in roads[curr]:
                    if visited[to] == 0:
                        heapq.heappush(hq, (time+cost, to))
print(max(times))