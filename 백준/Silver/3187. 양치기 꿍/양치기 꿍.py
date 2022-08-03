from collections import deque

r, c = map(int, input().split())
areas = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
q = deque()
result = [0, 0]
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            visited[i][j] = 1
            sheep = 0
            wolf = 0
            q.append((i, j))
            while q:
                row, col = q.popleft()
                area = areas[row][col]
                if area == '#':
                    continue
                    
                elif area == 'v':
                    wolf += 1
                    
                elif area == 'k':
                    sheep += 1
                    
                for move in moves:
                    move_r = row + move[0]
                    move_c = col + move[1]
                    if move_r < 0 or move_r >= r or move_c < 0 or move_c >= c:
                        continue
                        
                    if visited[move_r][move_c] == 0:
                        visited[move_r][move_c] = 1
                        q.append((move_r, move_c))
            
            if sheep > wolf:
                result[0] += sheep
            else:
                result[1] += wolf
                
print(*result)