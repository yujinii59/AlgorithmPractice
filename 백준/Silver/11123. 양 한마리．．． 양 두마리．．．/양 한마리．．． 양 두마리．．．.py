from collections import deque

moves = [(-1,0), (1,0), (0,-1), (0,1)]
t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    maps = [input() for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and maps[i][j] == '#':
                visited[i][j] = 1
                cnt += 1
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    for move in moves:
                        move_r = r + move[0]
                        move_c = c + move[1]
                        if move_r < 0 or move_r >= h or move_c < 0 or move_c >= w:
                            continue
                        if visited[move_r][move_c] == 0 and maps[move_r][move_c] == '#':
                            visited[move_r][move_c] = 1
                            q.append((move_r, move_c))
    print(cnt)