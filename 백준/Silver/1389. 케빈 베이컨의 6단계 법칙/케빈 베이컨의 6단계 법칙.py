n, m = map(int, input().split())
conn = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    conn[a][b] = 1
    conn[b][a] = 1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        if conn[i][k] > 0:
            for j in range(i+1, n+1):
                if conn[k][j] > 0:
                    if conn[i][j] == 0:
                        conn[i][j] = conn[i][k] + conn[k][j]
                    else:
                        conn[i][j] = min(conn[i][j], conn[i][k] + conn[k][j])
                    
                    conn[j][i] = conn[i][j]

min_bacon = n ** 2
num = 0
for i in range(n):
    kevin = sum(conn[i+1])
    if min_bacon > kevin:
        num = i+1
        min_bacon = kevin

print(num)