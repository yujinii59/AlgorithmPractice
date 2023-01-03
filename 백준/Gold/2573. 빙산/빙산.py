from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(r)]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
time = 0
while cnt <= 1:
    cnt = 0
    visited = [[0] * c for _ in range(r)]
    tmp = deepcopy(heights)
    for i in range(r):
        if cnt > 1:
            break
        for j in range(c):
            if visited[i][j] == 0 and heights[i][j] > 0:
                cnt += 1
                if cnt > 1:
                    break

                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()

                    for move in moves:
                        mr = x + move[0]
                        mc = y + move[1]

                        if mr < 0 or mr >= r or mc < 0 or mc >= c:
                            continue
                        if heights[mr][mc] == 0:
                            tmp[x][y] = max(0, tmp[x][y] - 1)
                        else:
                            if visited[mr][mc] == 0:
                                visited[mr][mc] = 1
                                q.append((mr, mc))
    else:
        time += 1

    if cnt == 0:
        print(0)
        break

    heights = tmp

else:
    print(time)