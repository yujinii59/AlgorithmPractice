n = int(input())
matrix = [[1]*n for _ in range(n)]
total = 2*n
for i in range(1,n):
    for j in range(1, n):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        total += matrix[i][j]
        
print(total  % 1000000007, n ** 2)