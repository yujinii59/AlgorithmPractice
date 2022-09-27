from collections import deque
import sys

n = int(input())
fishes = []
loc = [0,0]
fish_cnt = 0
for i in range(n):
    sizes = list(map(int, sys.stdin.readline().split()))
    fishes.append(sizes)
    for j, size in enumerate(sizes):
        if size == 9:
            loc = [i, j]
        elif size > 0:
            fish_cnt += 1

time = 0
cnt = 2
size = 2
moves = [(0,-1),(0,1),(-1,0),(1,0)]
while fish_cnt:
    q = deque([(loc, 0, 0)])
    fishes[loc[0]][loc[1]] = 0
    visited = [[0]*n for _ in range(n)]
    visited[loc[0]][loc[1]] = 1
    min_dist = n*n+1
    blocks = []
    while q:
        curr, dist, s = q.popleft()
        if min_dist >= dist:
            if 0 < fishes[curr[0]][curr[1]] < size:
                min_dist = dist
                blocks.append(curr)

            for move in moves:
                mr = move[0] + curr[0]
                mc = move[1] + curr[1]
                if mr < 0 or mr >= n or mc < 0 or mc >= n:
                    continue
                if fishes[mr][mc] <= size and visited[mr][mc] == 0:
                    visited[mr][mc] = 1
                    q.append(((mr, mc), dist+1,fishes[mr][mc]))
    if min_dist <= n*n:
        fish_cnt -= 1
        cnt -= 1
        if cnt == 0:
            size += 1
            cnt = size
        time += min_dist
        block = sorted(blocks)[0]
        loc = block
    else:
        break
print(time)