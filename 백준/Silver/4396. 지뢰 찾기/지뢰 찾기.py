n = int(input())
arounds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# board = ['.'*8 for _ in range(n)]
bombs = []
for i in range(n):
    row = input()
    bombs.append(row)
#     for j in range(n):
#         if row[j] == '*':
#             for around in arounds:
#                 r = i+around[0]
#                 c = j+around[1]
#                 if r < 0 or r >= n or c < 0 or c >= n:
#                     continue
#                 board[r][c] += 1

flag = False
board = []
for i in range(n):
    row = input()
    board.append(list(row))
    if not flag:
        for j in range(n):
            if row[j] == 'x' and bombs[i][j] == '*':
                flag = True
                break

for i in range(n):
    for j in range(n):
        if board[i][j] == 'x':
            cnt = 0
            for around in arounds:
                r = i + around[0]
                c = j + around[1]
                if r < 0 or r >= n or c < 0 or c >= n:
                    continue
                if bombs[r][c] == '*':
                    cnt += 1
            board[i][j] = str(cnt)
        if bombs[i][j] == '*':
            if flag:
                print('*', end='')
            else:
                print('.', end='')
        else:
            print(board[i][j], end='')
    print()
