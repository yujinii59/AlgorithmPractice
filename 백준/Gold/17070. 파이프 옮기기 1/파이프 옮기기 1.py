n = int(input())
states = [list(map(int, input().split())) for _ in range(n)]
cases = [[[0,0,0] for _ in range(n)] for _ in range(n)]
cases[0][1][0] = 1
moves = {0: {0:(0,1), 2:(1,1)}, 1:{1:(1,0),2:(1,1)}, 2:{0:(0,1), 1:(1,0), 2:(1,1)}}
for i in range(n):
    for j in range(n):
        for k in range(3):
            case = cases[i][j][k]
            for direction, move in moves[k].items():
                mr = i + move[0]
                mc = j + move[1]
                if (mr >= n or mc >= n) or (states[mr][mc] == 1):
                    continue
                
                if direction == 2:
                    if states[i+1][j]+states[i][j+1] > 0:
                        continue
                cases[mr][mc][direction] += case
print(sum(cases[n-1][n-1]))