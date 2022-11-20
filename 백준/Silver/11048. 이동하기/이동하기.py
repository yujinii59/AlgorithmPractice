import sys

input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
candies = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        candies[i][j] = miro[i][j]
        add = []
        if i-1 >= 0:
            add.append(candies[i-1][j])
        if j-1 >= 0:
            add.append(candies[i][j-1])
        
        if len(add) == 2:
            add.append(candies[i-1][j-1])
            
        if add:
            candies[i][j] += max(add)
print(candies[n-1][m-1])