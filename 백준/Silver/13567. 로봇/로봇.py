import sys

moves = [(1, 0),(0,-1),(-1,0),(0,1)]
i = 0
m, n = map(int, sys.stdin.readline().split())
loc = [0,0]
boolean = True
for _ in range(n):
    cmd, num = sys.stdin.readline().split()
    if boolean:
        num = int(num)
        if cmd == 'TURN':
            if num == 0:
                i = (i-1) % 4
            else:
                i = (i+1) % 4
        else:
            for j in range(2):
                loc[j] += num * moves[i][j]
                if loc[j] < 0 or loc[j] > m:
                    boolean = False

if boolean:
    print(*loc)
else:
    print(-1)