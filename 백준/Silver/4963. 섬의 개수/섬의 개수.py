from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = -1
    while q:
        x, y = q.popleft()
        for i in range(-1, 2):
            for j in range(-1, 2):
                move_x = x + i
                move_y = y + j
                if move_x < 0 or move_x >= h or move_y < 0 or move_y >= w:
                    continue
                if maps[move_x][move_y] == 1:
                    maps[move_x][move_y] = -1
                    q.append((move_x, move_y))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                cnt += 1
                bfs(i, j)
                
    print(cnt)                    