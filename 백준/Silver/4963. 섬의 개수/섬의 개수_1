from collections import deque

moves = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    visited = [[0] * w for _ in range(h)]
    maps = [list(map(int, input().split())) for _ in range(h)]
    
    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = 1
                cnt += 1
                while q:
                    r, c = q.popleft()
                    for move in moves:
                        move_r = move[0] + r
                        move_c = move[1] + c
                        if move_r < 0 or move_r >= h or move_c < 0 or move_c >= w:
                            continue
                            
                        if maps[move_r][move_c] == 1 and visited[move_r][move_c] == 0:
                            q.append((move_r, move_c))
                            visited[move_r][move_c] = 1
    
    print(cnt)
