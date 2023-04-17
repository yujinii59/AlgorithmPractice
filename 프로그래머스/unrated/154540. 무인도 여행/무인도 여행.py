from collections import deque

def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]
    neighbor = [(-1,0),(1,0),(0,-1),(0,1)]
    stay_days = []
    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0 and maps[i][j] != 'X':
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                days = 0
                while q:
                    x, y = q.popleft()
                    days += int(maps[x][y])
                    for mr, mc in neighbor:
                        nr = mr + x
                        nc = mc + y
                        if nr < 0 or nr >= r or nc < 0 or nc >= c:
                            continue
                        if maps[nr][nc] != 'X' and visited[nr][nc] == 0:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                
                stay_days.append(days)
    
    if stay_days:
        answer = sorted(stay_days)
    else:
        answer = [-1]
                    
    return answer