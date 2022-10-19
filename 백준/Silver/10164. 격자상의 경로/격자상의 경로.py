def move_robot(h, w):
    maps = [[0]*(w+1) for _ in range(h+1)]
    maps[1][1] = 1
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                continue
            maps[i+1][j+1] = maps[i][j+1] + maps[i+1][j]
    return maps[h][w]

n, m, t = map(int, input().split())
if t == 0:
    print(move_robot(n, m))
else:
    q, r = divmod(t, m)
    if r == 0:
        r = m
        q -= 1
    print(move_robot(q+1, r) * move_robot(n-q, m-r+1))