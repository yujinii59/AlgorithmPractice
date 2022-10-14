from collections import deque

m, n = map(int, input().split())
q = deque()
visited = [[0]*n for _ in range(m)]
states = []
states.append(input())
for i, state in enumerate(states[0]):
    if state == '0':
        q.append((0, i))
        visited[0][i] = 1
        
for _ in range(m-1):
    states.append(input())

moves = [(0,-1),(0,1),(-1,0),(1,0)]
poss = False
while q:
    r, c = q.popleft()
    if r == m-1:
        poss = True
        break
    
    for move in moves:
        mr = r+move[0]
        mc = c+move[1]
        
        if mr < 0 or mr >= m or mc < 0 or mc >= n:
            continue
        
        if visited[mr][mc] == 0 and states[mr][mc] == '0':
            q.append((mr, mc))
            visited[mr][mc] = 1
            
if poss:
    print('YES')
else:
    print('NO')