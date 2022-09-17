from collections import deque
import sys

r, c = map(int, input().split())
spaces = []
safe_dists = deque()
dists = [[r*c]*c for _ in range(r)]
for i in range(r):
    states = list(map(int, sys.stdin.readline().split()))
    spaces.append(states)
    for j, state in enumerate(states):
        if state == 1:
            safe_dists.append((i, j, 0))
            dists[i][j] = 0

moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while safe_dists:
    dr, dc, dist = safe_dists.popleft()
    for move in moves:
        mr = move[0] + dr
        mc = move[1] + dc
        if mr < 0 or mr >= r or mc < 0 or mc >= c:
            continue
        if dists[mr][mc] > dist+1:
            dists[mr][mc] = dist+1
            safe_dists.append((mr, mc, dist+1))
        
max_dist = 0
for dist in dists:
    max_dist = max(max_dist, max(dist))

print(max_dist)
    