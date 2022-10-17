import sys
sys.setrecursionlimit(int(1e7))

def cases(r, c):
    global num_of_cases
#     print(num_of_cases, r, c)
    if num_of_cases[r][c] == 0:
        moves = [(0,1), (1,0), (1,1)]
        case = 0
        for move in moves:
            nr = r+move[0]
            nc = c+move[1]
            if nr >= n or nc >= m:
                continue
            case += cases(nr, nc)
        num_of_cases[r][c] = case % 1000000007
    return num_of_cases[r][c]
        

n, m = map(int, input().split())
num_of_cases = [[0]*m for _ in range(n)]
num_of_cases[n-1][m-1] = 1
cases(0,0)
print(num_of_cases[0][0])