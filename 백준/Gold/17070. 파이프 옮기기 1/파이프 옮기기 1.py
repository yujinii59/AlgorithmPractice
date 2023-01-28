moves = {
            'r':[(0,1,'r'), (1,1,'d')], 
            'c':[(1,0,'c'), (1,1,'d')], 
            'd':[(0,1,'r'), (1,0,'c'), (1,1,'d')]
        }

cases = {}
def dfs(direction, x, y):
    cnt = 0
    if x == n-1 and y == n-1:
        cnt = 1
    elif (x, y, direction) in cases:
        cnt = cases[(x, y, direction)]
    else:
        for move in moves[direction]:
            move_x = x + move[0]
            move_y = y + move[1]
            direct = move[2]
            if move_x >= n or move_y >= n:
                continue
                
            if direct == 'd':
                if maps[move_x][move_y] == 0 and maps[move_x - 1][move_y] == 0 and maps[move_x][move_y - 1] == 0:
                    cnt += dfs(direct, move_x, move_y)
            else:
                if maps[move_x][move_y] == 0:
                    cnt += dfs(direct, move_x, move_y)
                    
        cases[(x, y, direction)] = cnt                
    return cnt


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
    
cnt = dfs('r', 0, 1)
print(cnt)