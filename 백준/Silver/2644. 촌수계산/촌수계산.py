n = int(input())
relations = [[-1 for i in range(n+1)] for i in range(n+1)]
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    p, c = map(int, input().split())
    relations[p][c] = 1
    relations[c][p] = 1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        if relations[i][k] > 0:
            for j in range(i, n+1):
                if relations[k][j] > 0:
                    tmp = relations[i][k] + relations[k][j]
                    if relations[i][j] > 0:
                        relations[i][j] = min(relations[i][j], tmp)
                        relations[j][i] = relations[i][j]
                    else:
                        relations[i][j] = tmp
                        relations[j][i] = tmp
print(relations[a][b])