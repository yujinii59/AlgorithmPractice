def dfs(r, c, num, cnt, set_number):
    if cnt == 6:
        set_number.add(num)
    else:
        for move in moves:
            move_r = r + move[0]
            move_c = c + move[1]
            if move_r < 0 or move_r >= 5 or move_c < 0 or move_c >= 5:
                continue
            
            set_number = dfs(move_r, move_c, num + board[move_r][move_c], cnt + 1, set_number)
    return set_number
            
board = [input().split() for _ in range(5)]
set_number = set()
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for i in range(5):
    for j in range(5):
        set_number = dfs(i, j, board[i][j], 1, set_number)
        
print(len(set_number))