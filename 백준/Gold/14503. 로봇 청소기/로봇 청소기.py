directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    # print(r, c, cnt)
    if maps[r][c] == 0:
        cnt += 1
        maps[r][c] = -1

    for i in range(4):
        d = (d - 1) % 4
        move = directions[d]
        mr = r + move[0]
        mc = c + move[1]
        if mr < 0 or mr >= n or mc < 0 or mc >= m:
            continue

        if maps[mr][mc] == 0:
            r = mr
            c = mc
            break
    else:
        back = directions[(d + 2) % 4]
        r += back[0]
        c += back[1]
        if r < 0 or r >= n or c < 0 or c >= m:
            break
        elif maps[r][c] == 1:
            break

print(cnt)