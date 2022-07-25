from collections import deque
import sys

n = int(input())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
q.append((0,0))
visited[0][0] = 0
p = False
while q:
    x, y = q.popleft()
    if x == n-1 and y == n-1:
        p = True
        break
    poss = maps[x][y]
    moves = [(poss, 0), (0, poss)]
    for move in moves:
        move_x = x + move[0]
        move_y = y + move[1]
        if move_x >= n or move_y >= n:
            continue
        if visited[move_x][move_y] == 0:
            q.append((move_x, move_y))
            visited[move_x][move_y] = 1
if p:
    print('HaruHaru')
else:
    print('Hing')