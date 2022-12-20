from collections import deque

r, c = map(int, input().split())
maps = [input() for _ in range(r)]
visited = [[0]*c for _ in range(r)]
moves = [(-1,0), (1,0), (0,-1), (0,1)]
cnt = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and maps[i][j] == '#':
            cnt += 1
            q = deque([(i, j)])
            visited[i][j] = 1
            while q:
                row, col = q.popleft()
                
                for move in moves:
                    mr = row + move[0]
                    mc = col + move[1]
                    if mr < 0 or mr >= r or mc < 0 or mc >= c:
                        continue
                    if visited[mr][mc] == 0 and maps[mr][mc] == '#':
                        visited[mr][mc] = 1
                        q.append((mr, mc))
print(cnt)