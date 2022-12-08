import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]

moves = [(-1,0), (1,0), (0,-1), (0,1)]
for i in range(r):
    for j in range(c):
        if maps[i][j] == '.':
            cnt = 0
            for move in moves:
                mr = i+move[0]
                mc = j+move[1]
                if mr < 0 or mr >= r or mc < 0 or mc >= c:
                    continue
                if maps[mr][mc] == '.':
                    cnt +=1
            
            if cnt <= 1:
                print(1)
                sys.exit(0)
print(0)