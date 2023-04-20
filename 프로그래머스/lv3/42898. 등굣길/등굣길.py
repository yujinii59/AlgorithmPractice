def solution(m, n, puddles):
    cases = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
                
            if i == 0 and j == 0:
                cases[i][j] = 1
            if 0 <= i-1 < n:
                cases[i][j] += cases[i-1][j]
            if 0 <= j-1 < m:
                cases[i][j] += cases[i][j-1]
            
            cases[i][j] %= 1000000007
            
    return cases[n-1][m-1]