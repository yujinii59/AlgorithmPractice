def dfs(height, row, col, h, w):
    cnt = 0
    if row == h - 1 and col == w - 1:
        cnt = 1
    else:
        for move in moves:
            move_r = move[0] + row
            move_c = move[1] + col
            if move_r < 0 or move_r >= h or move_c < 0 or move_c >= w:
                continue
            if maps[move_r][move_c] < height:
                if dp[move_r][move_c] >= 0:
                    cnt += dp[move_r][move_c]
                else:
                    cnt += dfs(maps[move_r][move_c],move_r, move_c, h, w)
    dp[row][col] = cnt
    return cnt

r, c = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
dp = [[-1] * c for _ in range(r)]
moves = [(-1,0),(1,0),(0,-1),(0,1)]
route_cnt = dfs(maps[0][0],0,0,r,c)
print(route_cnt)