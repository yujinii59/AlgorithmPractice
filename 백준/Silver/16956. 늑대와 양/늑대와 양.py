import sys

r, c = map(int, input().split())
maps = [list(input()) for i in range(r)]    

moves = [(-1,0), (1,0), (0,-1), (0,1)]
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            for move in moves:
                move_i = move[0] + i
                move_j = move[1] + j
                if move_i < 0 or move_i >= r or move_j < 0 or move_j >= c:
                    continue
                    
                if maps[move_i][move_j] == 'W':
                    print(0)
                    sys.exit()
                elif maps[move_i][move_j] == '.':
                    maps[move_i][move_j] = 'D'
            
print(1)
for m in maps:
    print(''.join(m))