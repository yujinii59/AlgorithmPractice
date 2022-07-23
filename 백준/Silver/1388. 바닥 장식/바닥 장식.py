n, m = map(int, input().split())
floor = [input() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
direction = {'-':(0, 1), '|':(1, 0)}
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt += 1
            shape = floor[i][j]
            d = direction[shape]
            r, c = i, j
            while True:
                r += d[0]
                c += d[1]
                if r >= n or c >= m:
                    break
                if visited[r][c] == 0 and floor[r][c] == shape:
                    visited[r][c] = 1
                else:
                    break
print(cnt)