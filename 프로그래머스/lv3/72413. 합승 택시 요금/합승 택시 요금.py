def solution(n, s, a, b, fares):
    INF = int(1e9)
    fees = [[INF]*(n+1) for _ in range(n+1)]
    for fare in fares:
        x, y, cost = fare
        fees[x][y] = cost
        fees[y][x] = cost
        
    for i in range(1, n+1):
        fees[i][i] = 0
        
    for k in range(1,n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                fees[i][j] = min(fees[i][j], fees[i][k]+fees[k][j])
                fees[j][i] = fees[i][j]
                
    taxi = [0] * (n+1)            
    for i in range(1, n+1):
        taxi[i] = fees[s][i] + fees[i][a] + fees[i][b]
        
    return min(taxi[1:])