from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    airplanes = {i+1:[] for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        airplanes[a].append(b)
        airplanes[b].append(a)
    
    visited = [0] * (n+1)
    q = deque()
    q.append(1)
    visited[1] = 1
    cnt = 0
    while q:
        loc = q.popleft()
        if sum(visited[1:]) == n:
            break
        
        for area in airplanes[loc]:
            if visited[area] == 0:
                visited[area] = 1
                cnt += 1
                q.append(area)
    print(cnt)