import heapq
import sys

input = sys.stdin.readline

n = int(input())
buses = {i+1: [] for i in range(n)}
for _ in range(int(input())):
    a, b, cost = map(int, input().split())
    buses[a].append((b, cost))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start, [start]))
visited = [0]*(n+1)
while q:
    cost, city, route = heapq.heappop(q)
    if visited[city]:
        continue
    visited[city] = 1
    if city == end:
        print(cost)
        print(len(route))
        print(*route)
        break
    
    for num, price in buses[city]:
        if visited[num] == 0:
            heapq.heappush(q, (cost+price, num, route+[num]))