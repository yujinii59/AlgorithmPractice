n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    if roads[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')