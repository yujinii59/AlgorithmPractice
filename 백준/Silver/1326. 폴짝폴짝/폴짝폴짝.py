from collections import deque

n = int(input())
visited = [0] * (n+1)
stones = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
q = deque([(0, a)])
cnt = -1
visited[a] = 1
while q:
    jump, stone = q.popleft()
    
    if stone == b:
        cnt = jump
        break
    
    remain = (n - stone) // stones[stone]
    for i in range(1, remain+1):
        loc = stone + i * stones[stone]
        if visited[loc] == 0:
            q.append((jump+1, loc))
            visited[loc] = 1

    remain = stone // stones[stone]
    for i in range(1, remain + 1):
        loc = stone - i * stones[stone]
        if loc > 0 and visited[loc] == 0:
            q.append((jump+1, loc))
            visited[loc] = 1
        

print(cnt)