from collections import deque

cnt = 0
n, m = map(int, input().split())
tomatoes = []
done = []
for i in range(m):
    blocks = list(map(int, input().split()))
    tomatoes.append(blocks)
    for j in range(n):
        if blocks[j] == 1:
            done.append((i, j, 0))
        elif blocks[j] == 0:
            cnt += 1

if cnt == 0:
    print(0)
else:
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque(done)
    day = -1
    while q:
        x, y, days = q.popleft()
        for move in moves:
            move_x = x + move[0]
            move_y = y + move[1]
            if move_x < 0 or move_x >= m or move_y < 0 or move_y >= n:
                continue
            if tomatoes[move_x][move_y] == 0:
                cnt -= 1
                tomatoes[move_x][move_y] = 1
                q.append((move_x, move_y, days + 1))
                if cnt == 0:
                    day = days + 1
                    break
    print(day)            