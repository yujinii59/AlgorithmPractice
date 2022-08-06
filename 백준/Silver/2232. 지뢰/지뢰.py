from collections import deque
import heapq

n = int(input())
heap = []
q = deque()
powers = []
for i in range(n):
    power = int(input())
    heapq.heappush(heap, (-power, i))
    powers.append(power)

bomb = []
while heap:
    power, loc = heapq.heappop(heap)
    if powers[loc] == -1:
        continue
    bomb.append(loc+1)
    q.append((loc, -power))
    while q:
        loc, power = q.popleft()
        powers[loc] = -1
        if loc > 0:
            if powers[loc-1] < power:
                q.append((loc-1, powers[loc-1]))
        if loc < n-1:
            if powers[loc+1] < power:
                q.append((loc+1, powers[loc+1]))
print(*sorted(bomb), sep='\n')