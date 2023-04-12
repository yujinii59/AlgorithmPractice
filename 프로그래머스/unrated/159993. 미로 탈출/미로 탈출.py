from copy import deepcopy
from collections import deque

def solution(maps):
    answer = 0
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]
    q = deque()
    for i, row in enumerate(maps):
        for j, state in enumerate(row):
            if state == 'L':
                q.append((i, j, 0))
                visited[i][j] = 1
    
    s_dist = -1
    e_dist = -1
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        i, j, cnt = q.popleft()
        if maps[i][j] == 'S':
            s_dist = cnt
        elif maps[i][j] == 'E':
            e_dist = cnt
            
        if s_dist >= 0 and e_dist >= 0:
            break
        
        for move in moves:
            nr = i + move[0]
            nc = j + move[1]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if visited[nr][nc] == 0 and maps[nr][nc] != 'X':
                visited[nr][nc] = 1
                q.append((nr, nc, cnt+1))
        
    if s_dist < 0 or e_dist < 0:
        return -1
    else:
        return s_dist + e_dist