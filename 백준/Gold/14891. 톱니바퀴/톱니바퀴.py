from collections import deque
# 2, 6
gears = []
for _  in range(4):
    gears.append(deque(list(input())))
k = int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    q = deque()
    q.append((num-1, direction))
    visited = [0]*4
    visited[num-1] = 1
    while q:
        n, d = q.popleft()
        
        if n+1 < 4 and visited[n+1] == 0:
            if gears[n][2] != gears[n+1][6]:
                q.append((n+1, -d))
                visited[n+1] = 1
                
        if n-1 >= 0 and visited[n-1] == 0:
            if gears[n][6] != gears[n-1][2]:
                q.append((n-1, -d))
                visited[n-1] = 1
                
        gears[n].rotate(d)

rst = 0
for i in range(4):
    if gears[i][0] == '1':
        rst += 2**i
        
print(rst)