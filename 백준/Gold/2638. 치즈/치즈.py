import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cheese_cnt = 0
maps = []
visited = []
for _ in range(n):
    visited.append([0]*m)
    row = list(map(int, input().split()))
    maps.append(row)
    for elem in row:
        if elem == 1:
            cheese_cnt += 1

if cheese_cnt:
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q =[]
    heapq.heappush(q, (0, 0,0))
    visited[0][0] = -1
    max_time = 0
    while q:
        if not cheese_cnt:
            print(max_time)
            break
        time, r, c = heapq.heappop(q)
        maps[r][c] = 0
        for move in moves:
            mr = r + move[0]
            mc = c + move[1]
            if mr < 0 or mr >= n or mc < 0 or mc >= m:
                continue
            if visited[mr][mc] == 0:
                if maps[mr][mc] == 0:
                    visited[mr][mc] = -1
                    heapq.heappush(q, (time, mr, mc))
                else:
                    visited[mr][mc] = 1
            elif visited[mr][mc] > 0:
                visited[mr][mc] += 1
                if visited[mr][mc] == 2:
                    visited[mr][mc] = -1
                    heapq.heappush(q, (time+1, mr, mc))
                    cheese_cnt -= 1
                    max_time = max(max_time, time+1)
        
        
else:
    print(0)
