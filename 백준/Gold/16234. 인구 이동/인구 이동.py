from copy import deepcopy
from collections import deque
import sys

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, l, u = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    tmp = deepcopy(maps)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                conn = []
                total = 0
                visited[i][j] = 1
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    conn.append((r, c))
                    total += maps[r][c]
                    for move in moves:
                        move_r = r + move[0]
                        move_c = c + move[1]

                        if move_r < 0 or move_r >= n or move_c < 0 or move_c >= n:
                            continue
                        diff = abs(maps[r][c] - maps[move_r][move_c])
                        if visited[move_r][move_c] == 0 and l <= diff <= u:
                            visited[move_r][move_c] = 2
                            q.append((move_r, move_c))

                length = len(conn)
                if length > 1:
                    num = total // length

                    for x, y in conn:
                        tmp[x][y] = num

    maps = tmp

    visit = []
    for v in visited:
        visit.extend(v)
    if len(set(visit)) == 1:
        break
    else:
        cnt += 1

print(cnt)