from collections import deque

conn = [(0, 1), (1, 0), (1,1)]
n, m = map(int, input().split())
maps = [input() for _ in range(n)]
q = deque([(0,0)])
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
cnt = 0
while q:
    r, c = q.popleft()
    prev = maps[r][c]
    
    if r % 2:
        conn[2] = (1, 1)
    else:
        conn[2] = (1, -1)
    
    for move in conn:
        mr = r+move[0]
        mc = c+move[1]
        
        if mr < 0 or mr >= n or mc < 0 or mc >= m:
            continue
        
        if maps[mr][mc] != prev and prev != '':
            cnt += 1
        
        if visited[mr][mc] == 0:
            visited[mr][mc] = 1
            q.append((mr, mc))
print(cnt)