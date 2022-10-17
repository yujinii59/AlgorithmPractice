from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
visited = []
for _ in range(n):
    maps.append(list(map(int, list(input().rstrip()))))
    visited.append([0]*m)

moves = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque()
# row, col, distance, break_wall(1: True, 2: False)
q.append((0,0,1,2))
visited[0][0] = 2
distance = -1
while q:
    r,c,dist,broken = q.popleft()
    if r == n-1 and c == m-1:
        distance = dist
        break
    
    for move in moves:
        mr = r+move[0]
        mc = c+move[1]
        if mr < 0 or mr >= n or mc < 0 or mc >= m:
            continue
        if maps[mr][mc] == 1:
            if broken == 2:
                q.append((mr, mc, dist+1, 1))
        else:
            if visited[mr][mc] < broken:
                visited[mr][mc] = broken
                q.append((mr, mc, dist+1, broken))
    
print(distance)